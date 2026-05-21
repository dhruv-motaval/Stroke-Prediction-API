import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load model and scaler
with open("best_stroke_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# Feature order used during training
FEATURE_COLUMNS = [
    "age",
    "hypertension",
    "heart_disease",
    "avg_glucose_level",
    "bmi",
    "gender_Male",
    "gender_Other",
    "ever_married_Yes",
    "work_type_Never_worked",
    "work_type_Private",
    "work_type_Self_employed",
    "work_type_children",
    "Residence_type_Urban",
    "smoking_status_formerly_smoked",
    "smoking_status_never_smoked",
    "smoking_status_smokes"
]

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

        input_dict = {
            "age": data.age,
            "hypertension": data.hypertension,
            "heart_disease": data.heart_disease,
            "avg_glucose_level": data.avg_glucose_level,
            "bmi": data.bmi,
            "gender_Male": data.gender_Male,
            "gender_Other": data.gender_Other,
            "ever_married_Yes": data.ever_married_Yes,
            "work_type_Never_worked": data.work_type_Never_worked,
            "work_type_Private": data.work_type_Private,
            "work_type_Self_employed": data.work_type_Self_employed,
            "work_type_children": data.work_type_children,
            "Residence_type_Urban": data.Residence_type_Urban,
            "smoking_status_formerly_smoked": data.smoking_status_formerly_smoked,
            "smoking_status_never_smoked": data.smoking_status_never_smoked,
            "smoking_status_smokes": data.smoking_status_smokes
        }

        # Create dataframe
        input_df = pd.DataFrame([input_dict])

        # Ensure correct column order
        input_df = input_df[FEATURE_COLUMNS]

        # Scale input
        input_scaled = scaler.transform(input_df)

        # Predict
        prediction = model.predict(input_scaled)[0]

        return {
            "prediction": int(prediction)
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/")
def home():
    return {
        "message": "Stroke Prediction API is running!"
    }
