import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


class TemplateZ(BaseModel):
    setup: str = Field(default="You are a helpful assistant.")
    punchline: str = Field(default="Give a clear and concise answer.")


template = TemplateZ()

output_parser = JsonOutputParser(pydantic_object=TemplateZ)

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("WATSONX_API_KEY"),
    temperature=0.5,
    top_p=0.2,
    top_k=1,
    max_output_tokens=256,
)

prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "{format_instructions}\n\n" + template.setup
    ),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{question}"),
]).partial(format_instructions=output_parser.get_format_instructions())

chain = prompt_template | gemini_llm | output_parser

response = chain.invoke({
    "question": "What is the capital of France?",
    "history": []
})

print(response)