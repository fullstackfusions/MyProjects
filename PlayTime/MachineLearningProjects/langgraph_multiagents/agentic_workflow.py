import os
import json
import operator
from enum import Enum, auto, unique
from typing import TypedDict, Annotated, Literal, List, Optional, Union, Type, Dict, Any

from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langchain_core.tools import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel, Field

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"

# Define Response Types and Models
@unique
class ResponseType(Enum):
    UNDEFINED = auto()
    TEXT = auto()
    TEMPLATE = auto()
    FORM = auto()

class Response(BaseModel):
    response_type: ResponseType = Field(default=ResponseType.UNDEFINED)

class TextResponse(BaseModel):
    text: str
    markdown: bool
    response_type: ResponseType = Field(default=ResponseType.TEXT)

class TemplateResponse(BaseModel):
    text: str
    template: str
    template_data: Union[list, Dict[str, Any]]
    response_type: ResponseType = Field(default=ResponseType.TEMPLATE)

class FormResponse(BaseModel):
    text: str
    form: str
    form_data: Union[list, Dict[str, Any]]
    response_type: ResponseType = Field(default=ResponseType.FORM)


# Define Tool Inputs
class CalculatorInput(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")

class MultiplierInput(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")

class ResearchInput(BaseModel):
    topic: str = Field(description="topic to research")

class ACIFabricsInput(BaseModel):
    fabric_name: Optional[str] = Field(default="name of the fabric")

class GreetingsInput(BaseModel):
    greeting: str = Field(description="The greeting to respond to")

class IntroductionInput(BaseModel):
    context: Optional[str] = Field(default="general", description="Context for the introduction")



# Define Tools
class CalculatorTool(BaseTool):
    name: str = "Calculator"
    description: str = "Adds two numbers"
    args_schema: Type[BaseModel] = CalculatorInput
    return_direct: bool = True

    def _run(self, a: int, b: int, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        result = a + b
        return TextResponse(text=f"Sum: {result}", markdown=False).model_dump_json()

class MultiplierTool(BaseTool):
    name: str = "Multiplier"
    description: str = "Multiplies two numbers"
    args_schema: Type[BaseModel] = MultiplierInput
    return_direct: bool = True

    def _run(self, a: int, b: int, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        result = a * b
        return TextResponse(text=f"Product: {result}", markdown=False).model_dump_json()

class ResearchTool(BaseTool):
    name: str = "Research"
    description: str = "Performs research on a topic"
    args_schema: Type[BaseModel] = ResearchInput
    return_direct: bool = True

    def _run(self, topic: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        result = f"Research on {topic}: got insights"
        return TemplateResponse(text="Research completed", template="research_template", template_data=result).model_dump_json()

class ACIFabricsTool(BaseTool):
    name: str = "ACIFabrics"
    description: str = "Gets ACI fabrics device info"
    args_schema: Type[BaseModel] = ACIFabricsInput
    return_direct: bool = True

    def _run(self, fabric_name: Optional[str], run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        result = "ACI fabric networks info" if not fabric_name else f"Filtered ACI info for {fabric_name}"
        return FormResponse(text="ACI query result", form="aci_fabric_form", form_data=result).model_dump_json()

class GreetingsTool(BaseTool):
    name: str = "Greetings"
    description: str = "Responds to user greetings"
    args_schema: Type[BaseModel] = GreetingsInput
    return_direct: bool = True

    def _run(self, greeting: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return TextResponse(text=f"Hello! How can I assist you today?", markdown=False).model_dump_json()

class IntroductionTool(BaseTool):
    name: str = "Introduction"
    description: str = "Provides an introduction to the chatbot's capabilities"
    args_schema: Type[BaseModel] = IntroductionInput
    return_direct: bool = True

    def _run(self, context: Optional[str], run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        intro = "I'm a chatbot designed to help with math calculations (addition, multiplication), research topics, and ACI fabrics info. Ask me anything related to these areas!"
        return TextResponse(text=intro, markdown=False).model_dump_json()

# Define Sub-Agent Toolsets
math_tools = [CalculatorTool(), MultiplierTool()]
research_tools = [ResearchTool()]
network_tools = [ACIFabricsTool()]
general_tools = [GreetingsTool(), IntroductionTool()]


# Define the LLM with Tools Bound for Each Sub-Agent
llm = ChatOpenAI(model="gpt-4o", temperature=0)
math_llm = llm.bind_tools(math_tools)
research_llm = llm.bind_tools(research_tools)
network_llm = llm.bind_tools(network_tools)
general_llm = llm.bind_tools(general_tools)


# Define State
class WorkflowState(TypedDict):
    query: str
    current_sub_agent: Annotated[Optional[Literal["math", "research", "network", "general"]], "Current sub-agent handling the task"]
    results: Annotated[List[str], operator.add]  # List of JSON responses from sub-agents
    fulfilled: Annotated[Optional[bool], "Whether the query is complete"]
    iteration: Annotated[int, "Current iteration count"]
    max_iterations: Annotated[int, "Maximum allowed iterations"]


# Define Pre-Filter Agent Node
def pre_filter_agent_node(state: WorkflowState) -> WorkflowState:
    messages = [
        HumanMessage(content=f"""You are a Pre-Filter Agent with reasoning capabilities. Your task is to:
            - If the query is a greeting (e.g., "Hello", "Hi"), set the sub-agent to "general" to handle it.
            - If the query is random or off-topic (not related to math, research, or ACI fabrics), set the sub-agent to "general" to provide an introduction.
            - If the query relates to math (e.g., addition, multiplication), research, or ACI fabrics, set the sub-agent to "math", "research", or "network" respectively.
            - Set "fulfilled" to true if "general" handles it completely, false otherwise.

            Query: {state['query']}

            Return a JSON object with "sub_agent" ("math", "research", "network", "general", or "none") and "fulfilled" (true/false) keys."""
        )
    ]
    response = llm.invoke(messages)
    decision = json.loads(response.content)

    return {
        "current_sub_agent": decision["sub_agent"] if decision["sub_agent"] != "none" else None,
        "fulfilled": decision["fulfilled"],
        "iteration": state["iteration"]
    }

# Define Central Agent Node
def central_agent_node(state: WorkflowState) -> WorkflowState:
    if state["iteration"] > state["max_iterations"]:
        return {
            "results": state["results"] + ["Max iterations reached. Could not fully process query."],
            "fulfilled": True,
            "iteration": state["iteration"]
        }

    messages = [
        HumanMessage(content=f"""You are a Central Agent managing sub-agents:
- math: Handles math queries (addition, multiplication) with Calculator and Multiplier tools.
- research: Handles research queries with the Research tool.
- network: Handles ACI fabrics queries with the ACIFabrics tool.

Given the query and current results, decide:
1. Which sub-agent should handle the next step ("math", "research", "network", or "none" if done or unknown).
2. Is the query fulfilled (true/false)?

Query: {state['query']}
Results: {json.dumps(state['results'])}

Return a JSON object with "sub_agent" and "fulfilled" keys.""")
    ]
    response = llm.invoke(messages)
    decision = json.loads(response.content)

    return {
        "current_sub_agent": decision["sub_agent"] if decision["sub_agent"] != "none" else None,
        "fulfilled": decision["fulfilled"],
        "iteration": state["iteration"] + 1
    }

# Define Sub-Agent Node
def sub_agent_node(state: WorkflowState) -> WorkflowState:
    sub_agent = state["current_sub_agent"]
    messages = [HumanMessage(content=state["query"])]

    if sub_agent == "math":
        response = math_llm.invoke(messages)
    elif sub_agent == "research":
        response = research_llm.invoke(messages)
    elif sub_agent == "network":
        response = network_llm.invoke(messages)
    elif sub_agent == "general":
        response = general_llm.invoke(messages)
    else:
        return state

    if response.tool_calls:
        tool_call = response.tool_calls[0]
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool = next(t for t in (math_tools + research_tools + network_tools + general_tools) if t.name == tool_name)
        tool_output = tool.invoke(tool_args)
        return {"results": [tool_output]}
    else:
        return {"results": ["No tool was called for this query."]}

# Define Routing Logic
def route_after_pre_filter(state: WorkflowState) -> str:
    if state["fulfilled"]:
        return END
    elif state["current_sub_agent"] == "general":
        return "sub_agent"
    elif state["current_sub_agent"] in ["math", "research", "network"]:
        return "central_agent"
    else:
        return {"results": state["results"] + ["I don't know how to handle this query."], "fulfilled": True}

def route_after_central(state: WorkflowState) -> str:
    if state["fulfilled"]:
        return END
    elif state["current_sub_agent"]:
        return "sub_agent"
    else:
        return {"results": state["results"] + ["I don't know how to handle this query."], "fulfilled": True}


# Build the Graph
workflow = StateGraph(WorkflowState)

# Add Nodes
workflow.add_node("pre_filter_agent", pre_filter_agent_node)
workflow.add_node("central_agent", central_agent_node)
workflow.add_node("sub_agent", sub_agent_node)

# Set Entry Point
workflow.set_entry_point("pre_filter_agent")

# Add Edges
workflow.add_conditional_edges("pre_filter_agent", route_after_pre_filter, {"central_agent": "central_agent", "sub_agent": "sub_agent", END: END})
workflow.add_conditional_edges("central_agent", route_after_central, {"sub_agent": "sub_agent", END: END})
workflow.add_edge("sub_agent", "central_agent")

# Compile the Graph
app = workflow.compile()



# Function to Run the Graph
def run_query(query: str) -> Union[Response, List[Response]]:
    initial_state = {
        "query": query,
        "current_sub_agent": None,
        "results": [],
        "fulfilled": False,
        "iteration": 0,
        "max_iterations": 5
    }
    result = app.invoke(initial_state)
    return load_response(result["results"])

def load_response(json_list: List[str]) -> Union[Response, List[Response]]:
    response_mapping = {
        ResponseType.TEXT.value: TextResponse,
        ResponseType.TEMPLATE.value: TemplateResponse,
        ResponseType.FORM.value: FormResponse,
    }

    responses = []
    for json_str in json_list:
        data = json.loads(json_str)
        response_type = data.get("response_type")
        model_cls = response_mapping.get(response_type, Response)
        responses.append(model_cls.model_validate_json(json_str))

    return responses if len(responses) > 1 else responses[0]

# Example Usage
if __name__ == "__main__":
    queries = [
        "Hello",
        "What is 2 + 3?",
        "Research about AI",
        "Get ACI fabrics info for fabric1",
        "What’s the weather like?"
    ]

    for query in queries:
        print(f"Query: {query}")
        output = run_query(query)
        print(f"Output: {json.dumps(output.model_dump() if isinstance(output, BaseModel) else [o.model_dump() for o in output], indent=2)}\n")
