# field_validator work in two mode - (i) Before Mode (ii) After Mode


from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight:float
    allergies: List[str] 
    contact_details: Dict[str, str]

    # use case of field_validator check the mail is end with hdfc.com or icici.com 
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def tranform_name(cls, value):
        return value.upper()
    
    # before mode of field_validator
    # @field_validator('age', mode='before')
    # @classmethod
    # def validate_age(cls, value):
    #     if 0<value<100:
    #         return value
    #     else:
    #         raise ValueError('Age must be in between 0 and 100')
        
    # the above code show an error because we can't compare 'str' and 'int'
    # after mode of field_validator (default value of mode is 'after')
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age must be in between 0 and 100')
        
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('updated into database')
patient_info = {'name':'saquib', 'email': 'abc@hdfc.com', 'age': '21', 'weight': 50.3,
                'allergies': ['pollen', 'dust'],
                'contact_details':{'phone': '9876543201'}}
patient1 = Patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)
