# This chain is able to execute the task in parallel and has fallback retry option

import logging
import json
from operator import itemgetter
from typing import Union, Any

# Langchain
from langchain_core.tools import tool
from langchain.output_parser import JsonOutputToolParser, CombiningOutputParser, PydanticToolsParser
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate, MesssagesPlaceholder
from langchain_core.utils.function_calling import convert_to_openai_function

from langchain_core.runnables import Runnable, RunnableLambda, RunnableMap, RunnablePassthrough, RunnableConfig
from exception import CustomToolException
from model import model
from tools import tools

logger = logging.getLogger(__name__)

def call_tool(tool_data: dict, config: RunnableConfig) -> None:
    """ Function for dynamically constructing the end of the chain based on the model-selected tool. """
    tool_map = {convert_to_openai_function(tool)["name"]: tool for tool in tools}
    response = {}
    tool_type = tool_map[tool_data["type"]]
    response["output"] = RunnableLambda(tool_type).with_retry(
        stop_after_attempt=5,
        wait_exponential_jitter=False
    ).invoke(tool_data["args"], config=config)

def handle_exception(inputs: dict) -> dict:
    exception = inputs.pop("exception")
    messages = [
        AIMessage(content="", additional_kwargs={"tool_args": [exception.tool_call]}),
        ToolMessage(tool_call_id=exception.tool_call["id"], content=str(exception.exception)),
        HumanMessage(content="The last tool calls raised exceptions. Try calling the tools again with corrected arguments."),
    ]
    inputs["last_output"] = messages
    return inputs

def response_parser(message: AIMessage):
    tool_calls = [dict(tc) for tc in message.tool_calls]
    for tc in tool_calls:
        tc["type"] - tc.pop("name")
    response_metadata = message.response_metadata
    response = {
        "tool_call": tool_calls[0],
        "response_metadata": response_metadata
    }
    return response

def tool_custom_exception(ai_message: dict, config: RunnableConfig) -> Runnable:
    try:
        return call_tool(tool_data=ai_message["tool_call"], config=config)
    except Exception as e:
        raise CustomToolException(tool_data=ai_message["tool_call"], exception=e)

prompt = ChatPromptTemplate.from_messages(
    [("human", "{input}", MesssagesPlaceholder("last_output", optional=True))]
)

model_with_tools = model.bind_tools(tools)

parallel_chain = prompt | model_with_tools | response_parser | tool_custom_exception

self_correcting_chain = parallel_chain.with_fallbacks(
    [handle_exception | parallel_chain], exception_key="exception"
)
