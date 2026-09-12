from langchain.schema import RunnableLambda
from langchain.prompts import PromptTemplate
from langchain.llms import Gemini
from langchain.output_parsers import StrOutputParser

template = "Tell me a {adjective} joke about {content}."
prompt_template = PromptTemplate(template=template, input_variables=["adjective", "content"])

# Function to format the prompt
def format_prompt(inputs):
    return prompt_template.format(**inputs)

# Create RunnableLambda to wrap the formatting function
format_runnable = RunnableLambda(format_prompt)

# Initialize the language model
llm = Gemini()

# Create the chain by connecting components with the pipe operator
chain = format_runnable | llm | StrOutputParser()

# Run the chain with input values
result = chain.invoke({"adjective": "funny", "content": "cats"})

print(result)