
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# Define State
class AgentState(TypedDict):
    message: str

# Node 1
def greeting_node(state: AgentState):
    return {
        "message": "Hello " + state["message"]
    }

# Node 2
def uppercase_node(state: AgentState):
    return {
        "message": state["message"].upper()
    }

# Create graph
graph_builder = StateGraph(AgentState)

# Register nodes
graph_builder.add_node("greeting", greeting_node)
graph_builder.add_node("uppercase", uppercase_node)

# Connect nodes
graph_builder.add_edge(START, "greeting")
graph_builder.add_edge("greeting", "uppercase")
graph_builder.add_edge("uppercase", END)

# Compile
graph = graph_builder.compile()

# Execute
result = graph.invoke({
    "message": "ByteForce"
})

print(result)
