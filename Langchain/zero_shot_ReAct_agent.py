import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ibm import ChatWatsonx


# Load .env
load_dotenv()


# Tool
@tool
def add_numbers_with_options(
    number: list[float],
    absolute: bool = False
) -> dict:
    """
    Adds a list of numbers provided by the user.
    If absolute is True, it adds the absolute values of the numbers.
    """

    if absolute:
        number = [abs(num) for num in number]

    total = sum(number)

    return {"result": total}


# IBM Watsonx Chat Model
llm = ChatWatsonx(
    model_id="Gemini 2.5 Flash",
    project_id=os.getenv("WATSONX_PROJECT_ID"),
    api_key=os.getenv("WATSONX_API_KEY"),
)

# Create agent
agent = create_agent(
    model=llm,
    tools=[add_numbers_with_options],
    system_prompt="You are a helpful assistant."
)


# User input
prompt = {
    "messages": [
        {
            "role": "user",
            "content": "Add 6, 8 and 9 using absolute values."
        }
    ]
}


# Run agent
response = agent.invoke(prompt)

print(response)