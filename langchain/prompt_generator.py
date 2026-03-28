from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
	template=
	"""
    my profession is {profession} and i have specialization in {domain}.
	so generate 20 lines of essay on every profession including specialization.
	things to focus on 
	1.dont include introduction of the profession and domain
	2.future scope 
	3.future demand 
	4.what are the pros and cons 
    """,
	input_variables=["profession","domain"],
	validate_template=True
)
template.save("template.json")