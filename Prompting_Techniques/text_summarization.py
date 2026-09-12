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

content = """
    The rapid advancement of technology in the 21st century has transformed various industries, including healthcare, education, and transportation. 
    Innovations such as artificial intelligence, machine learning, and the Internet of Things have revolutionized how we approach everyday tasks and complex problems. 
    For instance, AI-powered diagnostic tools are improving the accuracy and speed of medical diagnoses, while smart transportation systems are making cities more efficient and reducing traffic congestion. 
    Moreover, online learning platforms are making education more accessible to people around the world, breaking down geographical and financial barriers. 
    These technological developments are not only enhancing productivity but also contributing to a more interconnected and informed society.
"""

template = """Summarize the {content} in one sentence.
"""
prompt = PromptTemplate.from_template(template)

# Create the LCEL chain
summarize_chain = (
    RunnableLambda(format_prompt)
    | llm 
    | StrOutputParser()
)

# Run the chain
summary = summarize_chain.invoke({"content": content})
print(summary)