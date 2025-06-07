from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

response = model.invoke("Who is considered as one of the best batsmen in the world")

print(response.content)