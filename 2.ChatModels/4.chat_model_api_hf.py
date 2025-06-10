from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
print("Token found:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
llm = HuggingFaceEndpoint(
    repo_id='HuggingFaceH4/zephyr-7b-beta',
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Who is the inventor of 0?")
print(response)