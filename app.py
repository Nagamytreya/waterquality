import uvicorn
from fastapi import FastAPI
from waterq import Water
import numpy as np
import pickle
import pandas as Pd
app=FastAPI()
pickle_in=open('clsfr.pkl','rb')
classifier=pickle.load(pickle_in)

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
    if __name__=='__main__':
        uvicorn.run(app,host='120.0.0.1',port=8000)
#uvicorn app:app --reload
