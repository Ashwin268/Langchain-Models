from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

response = model.invoke("Suggest me some of best data science projects?")

print(response)

print(response.content)