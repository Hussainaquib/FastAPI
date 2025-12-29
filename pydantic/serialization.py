from pydantic import BaseModel

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

# for dictionary conversion (can be able to fetch/discard only one or more than one type of field using include and exclude)
temp=patient1.model_dump(include=['name']) 
# temp=patient1.model_dump_json() # for json conversion
print(temp)
print(type(temp))

