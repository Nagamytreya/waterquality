import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as Pd
from pydantic import BaseModel
app=FastAPI()
pickle_in=open('clsfr.pkl','rb')
classifier=pickle.load(pickle_in)

class Water(BaseModel):
    ph:float
    Hardness:float
    Solids:float
    Chloramines:float
    Sulfate:float
    Conductivity:float
    Organic_carbon:float
    Trihalomethanes:float
    Turbidity:float

@app.get('/')
def index():
    return{"message":'Hello,stranger'}
@app.get('/{name')
def get_name(name:str):
    return{'message':f'Hello,{name}'}
@app.post('/predict')
def predict_water(data:Water):
    data=data.dict()
    print(data)
    ph=data['ph']
    Hardness=data['Hardness']
    Solids=data['Solids']
    Chloramines=data['Chloramines']
    Sulfate=data['Sulfate']
    Conductivity=data['Sulfate']
    Organic_carbon=data['Organic_carbon']
    Trihalomethanes=data['Trihalomethanes']
    Turbidity=data['Turbidity']
    #   print(classifier.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]]))
    prediction=classifier.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])
    if(prediction[0]>0.5):
        prediction="Good water"
    else:
        prediction="Bad water"
    return{
        'prediction':prediction
    }
  
