from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = HuggingFacePipeline.from_model_id(
	model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
	pipeline_kwargs={
        "max_new_tokens": 100000000,
        "temperature": 0.7,
    }
)
chat_model = ChatHuggingFace(llm=model) 
parser = JsonOutputParser()
response  = chat_model.invoke("what is ai")
result = parser.invoke(response)
print(result)

 