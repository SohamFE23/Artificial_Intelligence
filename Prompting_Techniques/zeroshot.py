import os

from langchain_google_genai import ChatGoogleGenerativeAI


def llm_model(prompt_txt, params=None):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Please set the GOOGLE_API_KEY environment variable before running this script.")

    default_params = {
        "temperature": 0.5,
        "top_p": 0.2,
        "top_k": 1,
        "max_output_tokens": 256,
    }

    if params:
        default_params.update(params)

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key,
        temperature=default_params["temperature"],
        top_p=default_params["top_p"],
        top_k=default_params["top_k"],
        max_output_tokens=default_params["max_output_tokens"],
    )

    response = llm.invoke(prompt_txt)
    return response.content if hasattr(response, "content") else str(response)


params = {
    "temperature": 0.5,
    "top_p": 0.2,
    "top_k": 1,
    "max_output_tokens": 128,
}

prompt = """Classify the following statement as true or false:
'The Eiffel Tower is located in Berlin.'

Answer:
"""

response = llm_model(prompt, params)
print(f"prompt:\n{prompt}\n")
print(f"response:\n{response}\n")