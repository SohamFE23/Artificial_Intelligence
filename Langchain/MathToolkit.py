from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ibm import Gemini

load_dotenv()

@tool
def sum_nums(
    number:list[float],
    absolute :bool=False
) -> dict:
    """
    Adds a list of numbers provided by the user.
    If absolute is True, it adds the absolute values of the numbers.
    """
    if absolute:
        number = [abs(num) for num in number]

    total = sum(number)
    return {"result": total}

def subtract_nums(
    number: list[float],
    absolute: bool = False
) -> dict:
    """
    Subtracts a list of numbers provided by the user. 
    If absolute is True, it subtracts the absolute value of the numbers.
    """
    if absolute:
        number = [abs(num) for num in number]
    total=number[0]
    for num in number[1]:
        total -= num
    return {"result": total}

def multiply_nums(
    number:list[float],
    absolute:bool=False
) -> dict:
    """
    Multiplies a list of numbers provided by the user.
    """
    if absolute:
        number = [abs(num) for num in number]

    total=1
    for num in number:
        total *=num

    return {"result": total}

llm =Gemini(
    model_id="Gemini 2.5 Flash",
    project_id=os.getenv("WATSONX_PROJECT_ID"),
    api_key=os.getenv("WATSONX_API_KEY"),
)

add_agent=create_react_agent(
    model=llm,
    tools=[sum_numbers_with_complex_output],
    system_prompt="You are a helpful mathematical asistant that can perform various calculations.Use the Tools precisely and explain your reasoing clearly."
)

response=add_agent.invoke(
    {"messages": [("human","Add the numbers -10,-20,-30")]}
)

final_answer=response["messages"][-1].content
final_answer: {"result": -60.0}