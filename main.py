from numpy import require
from model import local_llm
from langchain import globals
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from pydantic import BaseModel,Field
from typing import Annotated, TypedDict ,Literal
from Allprompts.prompts import *

globals.set_verbose(True)
globals.set_debug(True)

class State(TypedDict):
    messages:Annotated[list[str],add_messages]
    plan:str
    Approval:Literal["YES","NO"]
    feedback:str
    code:str

class Feedback(BaseModel):
    Approval: Literal["YES", "NO"] = Field(
        description="Decide if the generated code has any bugs or issues. NO if it has bugs else YES",
    )
    Feedback: str = Field(
        description="suggestions to fix the errors in the code if the feedback value is NO",
    )

def planner_agent(state:State)->dict:
    prompt=planner_prompt_template(state["messages"])
    res=local_llm().invoke(prompt)
    return {"plan":res}

def coder_agent(state:State)->dict:
    plan=state["plan"]
    feedback=state.get("feedback","")
    print("feedback : ",feedback)
    if not feedback or state.get("feedback","")=="":
        res=local_llm().invoke(coder_prompt_template(plan))
        return {"code":res}
    else:
        res=local_llm().invoke(coder_prompt_withfeedback_template(plan,feedback))
        return {"code":res}
    
def evaluator_agent(state:State)->dict|None:
    code=state.get("code","")
    llm=local_llm().with_structured_output(Feedback)
    if code:
        res=llm.invoke(evaluator_prompt_template(code))
        return {"Approval":res.Approval,"feedback":res.Feedback}

def route_if_improvements_require(state:State)->str|None:
    if(state.get("Approval","")=="YES"):
        return "Accepted"
    elif(state.get("Approval","")=="NO"):
        return "Rejected+feedback"

graph=StateGraph(State)

graph.add_node("planner_agent",planner_agent) 
graph.add_node("coder_agent",coder_agent) 
graph.add_node("evaluator_agent",evaluator_agent) 
graph.add_edge(START,"planner_agent")
graph.add_edge("planner_agent","coder_agent")
graph.add_edge("coder_agent","evaluator_agent")
graph.add_conditional_edges(
    "evaluator_agent",
    route_if_improvements_require,
    {
        "Accepted": END,
        "Rejected+feedback": "coder_agent",
    },
)
graph.add_edge("coder_agent",END)
flow=graph.compile()

# llm_with_structured_output=local_llm().with_structured_output(Feedback)


if __name__ == "__main__":
    def main():
        res=flow.invoke({"messages":"write a simple factorial program in any language"})
        print(res)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("Just the code : ")
        code=res["code"].content
        print(code)
    main()
