from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='openbmb/MiniCPM4-0.5B',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("Who is the CEO of Microsoft")