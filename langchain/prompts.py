from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')
profession = input("Enter the profession")
domain = input("Enter the domain")

template = load_prompt('template.json')
prompt = template.invoke({
	"profession": profession,
	"domain": domain
})

result = model.invoke(prompt)
print(result.content)
