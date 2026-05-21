import pickle
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Load the trained model and scaler
with open("best_stroke_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# ✅ Define input data schema
class StrokeInput(BaseModel):
    age: float
    hypertension: int
    heart_disease: int
    avg_glucose_level: float
    bmi: float
    gender_Male: int
    gender_Other: int
    ever_married_Yes: int
    work_type_Never_worked: int
    work_type_Private: int
    work_type_Self_employed: int
    work_type_children: int
    Residence_type_Urban: int
    smoking_status_formerly_smoked: int
    smoking_status_never_smoked: int
    smoking_status_smokes: int

@app.post("/predict")
async def predict(data: StrokeInput):
    try:
        # ✅ Convert input to NumPy array
        input_data = np.array([[
            data.age, data.hypertension, data.heart_disease,
            data.avg_glucose_level, data.bmi,
            data.gender_Male, data.gender_Other,
            data.ever_married_Yes, data.work_type_Never_worked,
            data.work_type_Private, data.work_type_Self_employed,
            data.work_type_children, data.Residence_type_Urban,
            data.smoking_status_formerly_smoked, data.smoking_status_never_smoked,
            data.smoking_status_smokes
        ]])

        # ✅ Check input shape
        print("🔹 Input Features Shape:", input_data.shape)
        print("🔹 Scaler Expected Features:", scaler.n_features_in_)

        # ✅ Scale the input
        input_scaled = scaler.transform(input_data)

        # ✅ Make a prediction
        prediction = model.predict(input_scaled)[0]

        return {"prediction": int(prediction)}

    except Exception as e:
        return {"error": str(e)}

# ✅ Root endpoint
@app.get("/")
def home():
    return {"message": "Stroke Prediction API is running!"}
