from langchain_core.messages import ToolCall

class CustomToolException(Exception):
    def __init__(self, tool_data: ToolCall, exception: Exception) -> None:
        super().__init__()
        self.tool_data = tool_data
        self.exception = exception
