from pydantic import BaseModel

class Student(BaseModel):
	name:str
	age: str

new_student = {'name':'Sahil','age':20}

result = Student(**new_student)
print(result)