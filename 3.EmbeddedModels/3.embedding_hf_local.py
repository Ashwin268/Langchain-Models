from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

docs = {
    "Bengaluru is capital of Karnataka",
    "Ahemdbad is capital of Gujurat",
    "Chennai is capital of Tamil nadu"
}

vector = embedding.embed_documents(docs)

print(str(vector))