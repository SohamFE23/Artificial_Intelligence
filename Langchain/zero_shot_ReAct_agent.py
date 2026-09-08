from langchain.agents import initialize_agent
##becomed older

from langchain.agents import create_agent
from langchain.tools import StructuredTool
from langchain.llms import IBMWatsonxAI

def add_numbers_with_options(number: list[float],absolute: bool = False) -> dict:
    """
    Adds a list of numbers provided by the user. If absolute is set to True, it will add the absolute values of the numbers.
    """
    if absolute:
        number = [abs(num) for num in number]
    total = sum(number)
    return {"result": total}

    #Wrap the functions as a StruturedTool
    add_tool= StructuredTool.from_function(
        add_numbers_with_options,
        name="add_numbers_with_options",
        description="Adds a list of numbers provided by the user. If absolute is set to True, it will add the absolute values of the numbers."
    )

    llm= IBMWatsonxAI(
        model_name="granite-13b-chat-v2"
    )

    #Initialz the structured zero-shot ReAct agent
    agent=initialize_agent(
        tools=[add_tool],
        llm=llm,
        agent_type="structured_zero_shot_react_description",
        verbose=True
    )

    #Example input prompt to the agent
    prompt= {
        "input": {
            "numbers":{6,8,9},
            absolute: True
        }
    }

    #Call the agent
    response = agent.revoke(prompt)
    print("Agent Response:", response["output"])