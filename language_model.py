from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


parser = StrOutputParser()
system_template = ("According to the following CV content, tell me only what's the name of the CV owner, "
                   "without no other text")
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{user_input}")]
)

model = Ollama(model="llama3.1")

chain = prompt_template | model
print(chain.invoke({"user_input": "Hi, this CV is for Arash Sayareh"}))