from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()

model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")

messages =[
	SystemMessage(content="You are a chatassistance"),
	HumanMessage(content="Hello tell me about the chat ethics")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)