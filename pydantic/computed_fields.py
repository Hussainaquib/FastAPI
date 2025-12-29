# computed_fields: calculation on two or more field then find/create new field in run time

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight:float # kg
    height:float # meter
    allergies: List[str] 
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi= round(self.weight/(self.height**2),2)
        return bmi

        
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print('BMI', patient.bmi)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated into database')
patient_info = {'name':'saquib', 'email': 'abc@hdfc.com', 'age': '65', 'weight': 50.3, 'height': 1.72,
                'allergies': ['pollen', 'dust'],
                'contact_details':{'phone': '9876543201', 'emergency': '9876543217'}}
patient1 = Patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)
