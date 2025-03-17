from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd
from pydantic import BaseModel

# Load the trained model
model = joblib.load("churn_model.pkl")

# Define FastAPI app
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define request body model
class ChurnPredictionRequest(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str
    InternetService: str
    PaymentMethod: str
    SeniorCitizen: int
    OnlineSecurity: str
    TechSupport: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(data: ChurnPredictionRequest):
    try:
        print(f"Received data: {data}")
        # Convert input data to DataFrame
        input_data = pd.DataFrame([data.dict()])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        return {"churn_prediction": bool(prediction), "churn_probability": probability}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
