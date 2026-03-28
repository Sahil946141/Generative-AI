from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

template1= PromptTemplate(
	template='give me details about {topic}',
	input_variables=['topic'] 
)

template2 = PromptTemplate(
	template='generate a 5 line summary from the response {text}',
	input_variables=['text']
)
model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Virat Kohli'})

print(result)

chain.get_graph().print_ascii()

