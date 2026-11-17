
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# 1. Define the State
class AgentState(TypedDict):
    message: str


# 2. Define the Node
def greeting_node(state: AgentState):
    return {
        "message": "Hello " + state["message"]
    }


# 3. Create the Graph
graph_builder = StateGraph(AgentState)


# 4. Add the Node
graph_builder.add_node("greeting", greeting_node)


# 5. Define the Edges
graph_builder.add_edge(START, "greeting")
graph_builder.add_edge("greeting", END)


# 6. Compile the Graph
graph = graph_builder.compile()


# 7. Execute the Graph
result = graph.invoke({
    "message": "ByteForce"
})


# 8. Print the Result
print(result)
