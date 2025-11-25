from fastapi import FastAPI

app = FastAPI() #Creates the app instance

@app.get("/") #Defines a GET route on root
def hello_world():
    return {'message': 'Hello World'} #Response in JSON format