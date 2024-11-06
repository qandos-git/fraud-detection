from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

with open('artifacts/fraud_detection_model.pkl', 'rb') as m:
    model = pickle.load(m)

class Example(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float


@app.post('/')
def detect_fraud(x: Example):
    df = pd.DataFrame([x.dict()])
    prediction = model.predict(df)
    prediction = int(prediction[0])
    return  {"result": prediction}