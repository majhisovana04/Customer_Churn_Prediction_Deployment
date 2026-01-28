import streamlit as st
import requests
import numpy as np
import base64
from pathlib import Path
def add_background(image_path):
    image_bytes = Path(image_path).read_bytes()
    encoded = base64.b64encode(image_bytes).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: 
                linear-gradient(
                    rgba(0, 0, 0, 0.65),
                    rgba(0, 0, 0, 0.65)
                ),
                url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    
add_background("assests/background.jpg")
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# ---------------- STYLES ----------------
st.markdown("""
<style>

/* Feature labels: white text + deep red outline */
label,
.stSelectbox label,
.stNumberInput label,
.stTextInput label {
    color: #ffffff !important;
    font-weight: 600;
    background: transparent !important;
    padding: 0 !important;

    /* Deep red outline effect */
    text-shadow:
        -1px -1px 0 #7f1d1d,
         1px -1px 0 #7f1d1d,
        -1px  1px 0 #7f1d1d,
         1px  1px 0 #7f1d1d,
         0px  0px 6px rgba(220, 38, 38, 0.6);
}

/* Remove Streamlit label containers */
div[data-testid="stWidgetLabel"] {
    background: transparent !important;
}

/* Optional: inputs red focus glow */
.stSelectbox div[data-baseweb="select"]:focus-within,
.stNumberInput input:focus {
    box-shadow: 0 0 0 2px rgba(220, 38, 38, 0.6) !important;
    border-radius: 12px;
}
            
/* ===== PREDICT BUTTON (NEW – BLUE EFFECT) ===== */
.stButton > button {
    width: 100%;
    height: 3.2em;
    border-radius: 16px;
    border: 2px solid #38bdf8;
    background: linear-gradient(135deg, #020617, #020617);
    color: #e0f2fe;
    font-size: 1.1rem;
    font-weight: 800;
    letter-spacing: 0.6px;
    box-shadow:
        0 0 12px rgba(56,189,248,0.35),
        inset 0 0 14px rgba(56,189,248,0.15);
    position: relative;
    overflow: hidden;
    transition: all 0.35s ease;
}

.stButton > button::before {
    content: "";
    position: absolute;
    top: 0;
    left: -120%;
    width: 120%;
    height: 100%;
    background: linear-gradient(
        120deg,
        transparent,
        rgba(56,189,248,0.35),
        transparent
    );
    transition: all 0.6s ease;
}

.stButton > button:hover::before {
    left: 120%;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.03);
    box-shadow:
        0 0 22px rgba(56,189,248,0.8),
        0 0 42px rgba(56,189,248,0.6);
}

.stButton > button:active {
    transform: scale(0.97);
    box-shadow: 0 0 16px rgba(56,189,248,0.6);
}

</style>
""", unsafe_allow_html=True)



# ---------------- TITLE ----------------
st.markdown("""
<style>

/* TITLE EFFECT */
.title-glow {
    text-align: center;
    color: #ffffff;
    font-weight: 900;
    letter-spacing: 1px;

    text-shadow:
        0 0 5px rgba(255,255,255,0.6),
        0 0 12px rgba(220,38,38,0.6),
        0 0 22px rgba(127,29,29,0.9);

    animation: pulseGlow 3s infinite ease-in-out;
}

/* Glow breathing animation */
@keyframes pulseGlow {
    0% {
        text-shadow:
            0 0 6px rgba(255,255,255,0.5),
            0 0 14px rgba(220,38,38,0.6),
            0 0 26px rgba(127,29,29,0.8);
    }
    50% {
        text-shadow:
            0 0 10px rgba(255,255,255,0.9),
            0 0 20px rgba(239,68,68,0.9),
            0 0 36px rgba(127,29,29,1);
    }
    100% {
        text-shadow:
            0 0 6px rgba(255,255,255,0.5),
            0 0 14px rgba(220,38,38,0.6),
            0 0 26px rgba(127,29,29,0.8);
    }
}

</style>
""", unsafe_allow_html=True)
st.markdown(
    "<h1 class='title-glow'>📊 Customer Churn Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:#e5e7eb;font-weight:500;margin-top:-10px;'>Predict customer churn using ML</p>",
    unsafe_allow_html=True
)


st.markdown("<div class='card'>", unsafe_allow_html=True)

# ---------------- USER INPUTS ----------------
SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
Partner = st.selectbox("Has Partner?", ["No", "Yes"])
Dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
tenure = st.number_input("Tenure (months)", min_value=0, step=1)
OnlineSecurity = st.selectbox("Online Security", ["No", "Yes"])
TechSupport = st.selectbox("Tech Support", ["No", "Yes"])

Contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

PaperlessBilling = st.selectbox("Paperless Billing", ["No", "Yes"])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0)

# ---------------- ENCODING ----------------
binary_map = {"No": 0, "Yes": 1}
contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

payload = {
    "SeniorCitizen": binary_map[SeniorCitizen],
    "Partner": binary_map[Partner],
    "Dependents": binary_map[Dependents],
    "tenure": tenure,
    "OnlineSecurity": binary_map[OnlineSecurity],
    "TechSupport": binary_map[TechSupport],
    "Contract": contract_map[Contract],
    "PaperlessBilling": binary_map[PaperlessBilling],
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

# ---------------- PREDICTION ----------------
if st.button("Predict Churn"):
    try:
        # response = requests.post(
        #     "http://127.0.0.1:8000/predict",
        #     json=payload
        response=requests.post(
            "http://backend:8000/predict", 
            json=payload
        )

        

        if response.status_code == 200:
            result = response.json()
            if result["churn_prediction"] == 1:
                st.error(f"⚠️ Customer is likely to churn (Probability: {result['churn_probability']:.2f})")
            else:
                st.success(f"✅ Customer is NOT likely to churn (Probability: {result['churn_probability']:.2f})")
        else:
            st.error("❌ API Error")

    except Exception as e:
        st.error(f"❌ Connection error: {e}")

st.markdown("</div>", unsafe_allow_html=True)
