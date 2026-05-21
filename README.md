# 🫀 Stroke Risk Prediction API

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Space-yellow)

A machine learning API that predicts stroke risk from patient health data. Built with **FastAPI**, **Scikit-learn**, and **Docker** — deployed as a production-ready REST endpoint.

🔗 **Live Demo:** [huggingface.co/spaces/MotavalD/Stroke_Prediction](https://huggingface.co/spaces/MotavalD/Stroke_Prediction)

---

## What it does

Takes patient health indicators as input and returns a binary stroke risk prediction (0 = low risk, 1 = high risk). The model was trained on a healthcare stroke dataset with preprocessing, feature engineering, and class-imbalance handling.

---

## Tech stack

| Layer | Tool |
|---|---|
| API framework | FastAPI |
| ML model | Scikit-learn (best-performing classifier) |
| Preprocessing | Pandas, NumPy, StandardScaler |
| Serialization | Pickle |
| Deployment | Docker |

---

## Project structure

```
stroke-prediction/
│
├── app.py                  # FastAPI app with /predict endpoint
├── best_stroke_model.pkl   # Trained ML model
├── scaler.pkl              # Fitted StandardScaler
├── requirements.txt        # Dependencies
└── Dockerfile              # Container setup
```

---

## API usage

**Endpoint:** `POST /predict`

**Request body (JSON):**
```json
{
  "age": 67.0,
  "hypertension": 0,
  "heart_disease": 1,
  "avg_glucose_level": 228.69,
  "bmi": 36.6,
  "gender_Male": 1,
  "gender_Other": 0,
  "ever_married_Yes": 1,
  "work_type_Never_worked": 0,
  "work_type_Private": 1,
  "work_type_Self_employed": 0,
  "work_type_children": 0,
  "Residence_type_Urban": 0,
  "smoking_status_formerly_smoked": 1,
  "smoking_status_never_smoked": 0,
  "smoking_status_smokes": 0
}
```

**Response:**
```json
{
  "prediction": 1
}
```
`1` = high stroke risk, `0` = low stroke risk

---

## Input features explained

| Feature | Description |
|---|---|
| `age` | Patient age in years |
| `hypertension` | 1 if patient has hypertension |
| `heart_disease` | 1 if patient has heart disease |
| `avg_glucose_level` | Average blood glucose level (mg/dL) |
| `bmi` | Body mass index |
| `gender_Male` / `gender_Other` | One-hot encoded gender |
| `ever_married_Yes` | 1 if ever married |
| `work_type_*` | One-hot encoded work category |
| `Residence_type_Urban` | 1 if urban resident |
| `smoking_status_*` | One-hot encoded smoking history |

---

## Run locally

```bash
# Clone the repo
git clone https://github.com/dhruv-motaval/Stroke-Prediction-API
cd Stroke-Prediction-API

# Option 1 — Run with Docker
docker build -t stroke-api .
docker run -p 8000:8000 stroke-api

# Option 2 — Run directly
pip install -r requirements.txt
uvicorn app:app --reload

# Test the API
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 67, "hypertension": 0, "heart_disease": 1, "avg_glucose_level": 228.69, "bmi": 36.6, "gender_Male": 1, "gender_Other": 0, "ever_married_Yes": 1, "work_type_Never_worked": 0, "work_type_Private": 1, "work_type_Self_employed": 0, "work_type_children": 0, "Residence_type_Urban": 0, "smoking_status_formerly_smoked": 1, "smoking_status_never_smoked": 0, "smoking_status_smokes": 0}'
```

Interactive API docs available at `http://localhost:8000/docs` (FastAPI Swagger UI).

---

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check — confirms API is running |
| `POST` | `/predict` | Returns stroke risk prediction |

---

*Built by [Dhruv Motaval](https://www.linkedin.com/in/dhruv-motaval/) — B.Tech AI, Parul University*
