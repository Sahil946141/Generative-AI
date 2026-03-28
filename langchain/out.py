from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser,PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

class schema(BaseModel):
	Intro: str = Field(description='Introduction of Virat Kohli'),
	career:str = Field(description='Information as ap player'),
	matches: int = Field(description='Matches played'),
	captaincy:str = Field(description='info about captaincy')

parser = PydanticOutputParser(pydantic_object=schema)
template = PromptTemplate(
	template="Give me facts about {topic} \n {format_instruction}",
	input_variables=['topic'],
	partial_variables={'format_instruction': parser.get_format_instructions()}
)

response = template.invoke({'topic':'Virat Kohli'})
result = model.invoke(response) 

final_result = parser.invoke(result)

print(final_result)