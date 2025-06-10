from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

docs = {
    "Bengaluru is capital of Karnataka",
    "Ahemdbad is capital of Gujurat",
    "Chennai is capital of Tamil nadu"
}
result = embedding.embed_documents(docs)

print(str(result))

