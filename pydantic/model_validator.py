# model_validator apply on more than one field like age and contact_details

from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight:float
    allergies: List[str] 
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have an energency contact')
        return model

        
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated into database')
patient_info = {'name':'saquib', 'email': 'abc@hdfc.com', 'age': '65', 'weight': 50.3,
                'allergies': ['pollen', 'dust'],
                'contact_details':{'phone': '9876543201', 'emergency': '9876543217'}}
patient1 = Patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)
