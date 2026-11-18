from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import TypedDict
from tools import get_weather


load_dotenv()
class AgentState(TypedDict):
    message: str

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)
def llm_node(state: AgentState):

    response = llm.invoke(state["message"])

    return {
        "message": response.content
    }
llmtools=llm.bind_tools([get_weather])
graph_builder = StateGraph(AgentState)

graph_builder.add_node("llm", llm_node)

graph_builder.add_edge(START, "llm")
graph_builder.add_edge("llm", END)

graph = graph_builder.compile()
response=llmtools.invoke("Use weather tool to get the weather in Ontario")
print(response.tool_calls)