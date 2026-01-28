# 📊 Customer Churn Prediction App

## FastAPI + Streamlit + Docker
A complete end-to-end Customer Churn Prediction application using Machine Learning, containerized with Docker, featuring:
🚀 FastAPI backend for model inference
🎨 Streamlit frontend for user interaction
🐳 Docker & Docker Compose for deployment

## 🔍 Project Overview

Customer churn prediction helps businesses identify customers who are likely to leave.
This project uses a trained machine learning model to predict churn based on customer input data.
The system is split into two services:

A)Backend (FastAPI):
Handles model loading and prediction API.

B)Frontend (Streamlit):
Provides a user-friendly web interface.

Both services are containerized and run together using Docker Compose.

## 🧱 Project Structure:
```
Customer_Churn_Prediction_Deployment/
│
├── backend/
│   ├── churn_model.pkl
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── assets/
│   │   └── background.jpg
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── test_model.py
```
## ⚙️ Tech Stack
Python 3.11
FastAPI
Streamlit
Scikit-learn
Docker
Docker Compose

🚀 How to Run the Project (Docker)
1️⃣ Prerequisites
Make sure you have installed:
Docker
Docker Desktop (with WSL enabled on Windows)

2️⃣ Clone the Repository
git clone https://github.com/majhisovana04/Customer_Churn_Prediction_Deployment.git
cd Customer_Churn_Prediction_Deployment

3️⃣ Build & Run Containers
docker-compose up --build

4️⃣ Access the Application
Service	URL
Streamlit Frontend	http://localhost:8501
FastAPI Backend	http://localhost:8000
API Docs (Swagger)	http://localhost:8000/docs

📌 Key Features:
✅ ML model served via FastAPI
✅ Interactive UI with Streamlit
✅ Dockerized microservices
✅ Easy deployment with Docker Compose
✅ Clean & modular code structure
