# Nested Models
#1. better organisation of related data (e.g., vitals, address, insurance)
#2. Reusability: Use vitalsin multiple models (e.g., Patient, MedicalRecords)
#3. Readability: Easier for developer and API consumers to understand
#4. Validation: Nested Models are validated automatically no extrabwork needed


from pydantic import BaseModel
# from typing import List, Dict, Optional, Annotated

class Address(BaseModel):
    city:str
    state: str
    pin:str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address
        
address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}
address1=Address(**address_dict)

patient_dict={'name':'saquib', 'gender': 'male', 'age': 21, 'address': address1}
patient1=Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)


