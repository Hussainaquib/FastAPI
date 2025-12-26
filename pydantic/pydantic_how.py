# Steps in pydanti
##1. Define a pydantic model
##2. Instantiate the model with raw input data
##3. Pass the validated model object


#---------------------------------------------------------------------
# (I) Type Validation in pydantic


# (i) use case of BaseModel


# from pydantic import BaseModel
# class Patient(BaseModel):
#     name: str
#     age: int
# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('inserted into database')
# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('updated into database')
# patient_info = {'name':'saquib','age': '21'}
# patient1 = Patient(**patient_info)
# # insert_patient_data(patient1)
# update_patient_data(patient1)


# (ii) use cae of List, Dict and Optional in pydantic


# from pydantic import BaseModel
# from typing import List, Dict, Optional
# class Patient(BaseModel):
#     name: str
#     age: int
#     weight:float
#     allergies: Optional[List[str]] = None # making allergies optional
#     contact_details: Dict[str, str]
# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('inserted into database')
# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.weight)
#     print(patient.married)
#     print(patient.allergies)
#     print(patient.contact_details)
#     print('updated into database')
# patient_info = {'name':'saquib','age': '21', 'weight': 50.3, 'married':False,
#                 'contact_details':{'email':'abc@gmail.com', 'phone': '9876543201'}}
# patient1 = Patient(**patient_info)
# # insert_patient_data(patient1)
# update_patient_data(patient1)


#---------------------------------------------------------------------
# (II) Data Validation in pydantic


# (i) use case of EmailStr and AnyUrl (in built data validation in pydantic)


# from pydantic import BaseModel, EmailStr, AnyUrl
# from typing import List, Dict, Optional
# class Patient(BaseModel):
#     name: str
#     email: EmailStr
#     linkedin_url: AnyUrl
#     age: int
#     weight:float
#     allergies: Optional[List[str]] = None # making allergies optional
#     contact_details: Dict[str, str]
# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('inserted into database')
# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.email)
#     print(patient.linkedin_url)
#     print(patient.age)
#     print(patient.weight)
#     # print(patient.married)
#     print(patient.allergies)
#     print(patient.contact_details)
#     print('updated into database')
# patient_info = {'name':'saquib', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1322', 'age': '21', 'weight': 50.3,
#                 'contact_details':{'phone': '9876543201'}}
# patient1 = Patient(**patient_info)
# # insert_patient_data(patient1)
# update_patient_data(patient1)


# (ii) custom data validation in pydantic


from pydantic import BaseModel, EmailStr, AnyUrl, Field 
# Field function is for custom data validation, attached meta data (Field + Annotated)and for set default values
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    # name: str = Field(max_length=50) # set name length not greater than 50 Character using Field
    name: Annotated[str, Field(max_length=50, 
                               title='Name of the patient', 
                               description='Give the anme of the patient in less than 50 chars', 
                               examples=['saquib', 'amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int=Field(gt=0, lt=120) # set the range for the age using Field
    weight:Annotated[float, Field(gt=0, strict=True)] # set the weight value greater than zero using Field
    married: Annotated[bool, Field(default=None,
                                   description='Is the patient married or not')]
    # set number of allergies not greater than 5 and default value None
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)] 
    contact_details: Dict[str, str]
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated into database')
patient_info = {'name':'saquib', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1322', 'age': '21', 'weight': 50,
                'contact_details':{'phone': '9876543201'}}
patient1 = Patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)

