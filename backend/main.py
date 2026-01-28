# from fastapi import FastAPI
# import joblib
# import numpy as np
# from pydantic import BaseModel

# # Initialize app
# app = FastAPI(title="Customer Churn Prediction API")

# # Load model
# model = joblib.load("churn_model.pkl")

# # Input schema (10 features)
# class ChurnInput(BaseModel):
#     feature_1: float
#     feature_2: float
#     feature_3: float
#     feature_4: float
#     feature_5: float
#     feature_6: float
#     feature_7: float
#     feature_8: float
#     feature_9: float
#     feature_10: float


# @app.post("/predict")
# def predict_churn(data: ChurnInput):

#     input_data = np.array([[  
#         data.feature_1,
#         data.feature_2,
#         data.feature_3,
#         data.feature_4,
#         data.feature_5,
#         data.feature_6,
#         data.feature_7,
#         data.feature_8,
#         data.feature_9,
#         data.feature_10
#     ]])

#     prediction = model.predict(input_data)[0]
#     probability = model.predict_proba(input_data)[0][1]

#     return {
#         "churn_prediction": int(prediction),
#         "churn_probability": round(float(probability), 3)
#     }


from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# ---------------- INIT APP ----------------
app = FastAPI(title="Customer Churn Prediction API")

# ---------------- LOAD MODEL ----------------
model = joblib.load("churn_model.pkl")

# ---------------- INPUT SCHEMA ----------------
class ChurnInput(BaseModel):
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    OnlineSecurity: int
    TechSupport: int
    Contract: int
    PaperlessBilling: int
    MonthlyCharges: float
    TotalCharges: float

# ---------------- PREDICTION ENDPOINT ----------------
@app.post("/predict")
def predict_churn(data: ChurnInput):

    input_data = np.array([[  
        data.SeniorCitizen,
        data.Partner,
        data.Dependents,
        data.tenure,
        data.OnlineSecurity,
        data.TechSupport,
        data.Contract,
        data.PaperlessBilling,
        data.MonthlyCharges,
        data.TotalCharges
    ]])

    prediction = int(model.predict(input_data)[0])
    probability = float(model.predict_proba(input_data)[0][1])

    return {
        "churn_prediction": prediction,
        "churn_probability": round(probability, 3)
    }

