### Type Validation in python

# # Problem 1:
# def insert_patient_data(name,age):
#     print(name)
#     print(age)
#     print('inserted into database')
# insert_patient_data('saquib', 'thirty')

# # Problem 2:
# def insert_patient_data(name:str,age:int):
#     # it is still work because type hunting not produce error
#     print(name)
#     print(age)
#     print('inserted into database')
# insert_patient_data('saquib', '30')

# # Solution 1: enforce based raise error, but this method is not scalable
# def insert_patient_data(name:str,age:int):
#     if type(name)==str and type(age)==int:
#         print(name)
#         print(age)
#         print('inserted into database')

#     else:
#         raise TypeError('Incorrect Data')
# insert_patient_data('saquib', 30)

### By default python not have type validation, this problem is solved by pydantic

# -------------------------------------------------------------------------
### Data Validation in python

def insert_patient_data(name:str,age:int):
    if type(name)==str and type(age)==int:
        if age<0:
            raise ValueError('Age can not be nageative')
        else:
            print(name)
            print(age)
            print('inserted into database')

    else:
        raise TypeError('Incorrect Data')
insert_patient_data('saquib', -30)

### By default python not have data validation, this problem is solved by pydantic