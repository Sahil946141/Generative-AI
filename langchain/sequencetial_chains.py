from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

prompt1 = PromptTemplate(
	template="Give me the Joke about {topic}",
	input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
	template="Explain me the Joke {text}",
	input_variables=['text']
)

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result = chain.invoke({'topic': 'Virat Kohli'})

print(result)