from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser 


load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini ")
# llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

response = llm.invoke("What is a llm?")

print(response) 