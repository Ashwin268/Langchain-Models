from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro')

response = model.invoke('What is the capital city of Karnataka')

print(response.content)