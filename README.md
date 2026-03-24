# 🌾 AgriYield AI - Smart Crop Yield Prediction System

An AI-powered agriculture decision support system that predicts crop yield based on environmental conditions, soil nutrients, and farm parameters. The system provides actionable insights, fertilizer recommendations, and farm health indicators to assist farmers and stakeholders in improving agricultural productivity.

---

## 🔗 GitHub Repository
https://github.com/Shreya-pingle/AgriYield-Predictor-Forecasting-Crop-Yield-Using-Environmental-and-Soil-Data

## 🚀 Project Overview

AgriYield AI is a Machine Learning-based web application built using Streamlit that helps estimate crop yield (kg/hectare) using key agricultural factors such as:

- Soil nutrients (N, P, K)
- Weather conditions (rainfall, temperature, humidity)
- Farm management inputs (irrigation, area)
- Crop type, soil type, and location

The system not only predicts yield but also provides:

- 📊 Farm analytics dashboard  
- 🌿 Farm health indicators  
- 🧪 Fertilizer optimization suggestions  
- 📈 Yield improvement recommendations  
- 📄 Downloadable farm report  

---

## 🧠 Machine Learning Model

### Model Used:
- **Random Forest Regressor**

### Why Random Forest?
- Handles non-linear relationships
- Works well with tabular agricultural data
- Robust to noise and overfitting

### Model Performance:

| Metric | Value |
|------|------|
| R² Score | ~0.95 |
| MAE | ~97 |
| RMSE | ~121 |

---

## 📂 Dataset Details

The dataset includes agricultural features such as:

- State
- Crop
- Soil Type
- Year
- Rainfall (mm)
- Temperature (°C)
- Humidity (%)
- Nitrogen (kg/ha)
- Phosphorus (kg/ha)
- Potassium (kg/ha)
- Soil pH
- Irrigation Coverage (%)
- Area (hectares)

### Target Variable:
- **Yield (kg per hectare)**

## ⚙️ System Architecture
User Input (Streamlit UI)
↓
Data Preprocessing
↓
One-Hot Encoding
↓
Model Prediction (Random Forest)
↓
Output Dashboard + Insights


---

## 💻 Tech Stack

| Component | Technology |
|----------|----------|
| Frontend | Streamlit |
| Backend | Python |
| ML Model | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Visualization | Plotly |
| Model Storage | Joblib |
| Report Generation | FPDF |

---

## 🎯 Key Features

### 🌾 1. Crop Yield Prediction
Predicts yield in **kg/hectare** based on input parameters.

---

### 🌿 2. Farm Health Indicators

Calculated using input-based formulas:

- **Soil Fertility (%)** → Average of N, P, K  
- **Water Availability (%)** → Rainfall + Irrigation  
- **Weather Suitability (%)** → Temperature + Humidity  

---

### 🧪 3. Fertilizer Optimization

Provides intelligent suggestions:
- Low Nitrogen → Add nitrogen fertilizer
- Low Phosphorus → Add phosphate
- Low Potassium → Add potash

---

### 📈 4. Yield Improvement Suggestions

Recommends improvements such as:
- Increasing irrigation
- Adjusting soil pH
- Managing rainfall deficiency

---

### 📊 5. Farm Analytics Dashboard

Includes:
- Soil nutrient balance chart (kg/ha)
- Yield prediction gauge visualization
- History chart of all predictions 
---

### 📄 6. Downloadable Report

Generates a **PDF report** containing:
- Farm inputs
- Predicted yield
- Total production

---

## 📊 How Prediction Works

1. User inputs farm data
2. Data is encoded using one-hot encoding
3. Input is aligned with trained model features
4. Model predicts yield
5. Production is calculated:


Production = Yield × Area


---
---

## 🛠️ Installation & Setup

### Step 1: Clone Repository
---
bash
git clone https://github.com/Shreya-pingle/AgriYield-Predictor-Forecasting-Crop-Yield-Using-Environmental-and-Soil-Data
cd agriyield-ai

Step 2: Create Virtual Environment

python -m venv .venv
.venv\Scripts\activate
Step 3: Install Dependencies

pip install -r requirements.txt
Step 4: Run Application

python -m streamlit run app.py

📁 Project Structure

agriyield-ai/
├── app.py                  # Main Streamlit application
├── yield_model.pkl         # Trained ML model
├── dataset.xlsx            # Dataset
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

📌 Conclusion

AgriYield AI demonstrates how Machine Learning can be applied in agriculture to provide data-driven insights and support better farming decisions. 
It bridges the gap between traditional farming and modern AI technologies.
