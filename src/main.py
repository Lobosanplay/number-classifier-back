from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np
from scipy.ndimage import rotate
from service.modelNumberClassifier import create_model
import os

class NumberRequest(BaseModel):
    numbers: List[int]

app = FastAPI()

rnd_clf_model = None

@app.on_event("startup")
async def startup_event():
    """Se ejecuta al iniciar la aplicación"""
    global rnd_clf_model
    model_path = 'model/rnd_clf_model.pkl'
    
    try:
        if not os.path.exists(model_path):
            await create_model(model_path)
        
        rnd_clf_model = joblib.load(model_path)
        
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        raise
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],          
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.post('/')
def predict_react_number(request: NumberRequest):
    try:
        number = request.numbers
        number_np = np.array(number)
        number_reshaped = number_np.reshape(28,28)
        number_flip = np.flip(number_reshaped, 0)
        number_rotate = rotate(number_flip, angle=-90)
        number_clean = np.reshape(number_rotate, (1, 784))
        prediction = rnd_clf_model.predict(number_clean)
        return f'{prediction[0]}'
    except Exception as e:
        print(f"Hay un error de: {e}")