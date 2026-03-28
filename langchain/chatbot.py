from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()

chat_history = [
	SystemMessage(content="You are a chatbot")
]

model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")
while True:
	user_input = input("You: ")
	chat_history.append(HumanMessage(content=user_input))
	if user_input=='exit':
		break
	result = model.invoke(chat_history)
	chat_history.append(AIMessage(content=result.content))
	print("Ai: ",result.content)
print(chat_history)