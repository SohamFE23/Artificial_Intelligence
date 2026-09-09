#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo: LangChain agent with a custom tool, using Groq's OpenAI‑compatible API.
"""

import os
from dotenv import load_dotenv

# ----------------------------------------------------------------------
# 1️⃣  Load environment variables
# ----------------------------------------------------------------------
load_dotenv()                     # pulls values from .env into os.environ

# ----------------------------------------------------------------------
# 2️⃣  Define the custom tool (unchanged from your original example)
# ----------------------------------------------------------------------
from langchain_core.tools import tool

@tool
def add_numbers_with_options(
    number: list[float],
    absolute: bool = False,
) -> dict:
    """
    Adds a list of numbers provided by the user.
    If ``absolute`` is True, it adds the absolute values of the numbers.
    """
    if absolute:
        number = [abs(num) for num in number]

    total = sum(number)
    return {"result": total}


# ----------------------------------------------------------------------
# 3️⃣  Set up the Groq‑backed LLM
# ----------------------------------------------------------------------
from langchain_openai import ChatOpenAI

# Groq uses the same request format as OpenAI, but you must point the client
# at Groq’s endpoint and provide your Groq API key.
groq_llm = ChatOpenAI(
    # The model name you want to use on Groq – e.g. "mixtral-8x7b-32768"
    model="mixtral-8x7b-32768",
    # Groq's public OpenAI‑compatible endpoint
    base_url="https://api.groq.com/openai/v1",
    # Your secret key (read from the .env file)
    api_key=os.getenv("GROQ_API_KEY"),
    # Optional: tweak temperature, max tokens, etc.
    temperature=0.2,
    max_tokens=1024,
)

# ----------------------------------------------------------------------
# 4️⃣  Build the agent that can invoke the tool
# ----------------------------------------------------------------------
from langchain.agents import create_agent

agent = create_agent(
    model=groq_llm,
    tools=[add_numbers_with_options],
    # This system prompt will be sent to the LLM before the user message.
    system_prompt="You are a helpful assistant that can call tools when needed.",
)

# ----------------------------------------------------------------------
# 5️⃣  Prepare the user request (same structure you used before)
# ----------------------------------------------------------------------
prompt = {
    "messages": [
        {
            "role": "user",
            "content": "Add 6, 8 and 9 using absolute values."
        }
    ]
}

# ----------------------------------------------------------------------
# 6️⃣  Run the agent
# ----------------------------------------------------------------------
if __name__ == "__main__":
    response = agent.invoke(prompt)
    print("\n=== Agent response ===")
    print(response)