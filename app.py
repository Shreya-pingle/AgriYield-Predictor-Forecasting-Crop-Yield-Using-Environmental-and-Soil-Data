
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from fpdf import FPDF
import os
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AgriYield AI Predictor",
    page_icon="🌾",
    layout="wide"
)

# --------------------------------------------------
# UI THEME
# --------------------------------------------------

st.markdown("""
<style>
.stApp { background-color: #F4F8F2; }
p, span, label { color: #1B4332 !important; }
h1, h2, h3 { color: #1B4332 !important; }
[data-testid="stMetricValue"] {
    color: #1B4332;
    font-size: 32px;
    font-weight: bold;
}
section[data-testid="stSidebar"] {
    background-color: #E8F5E9;
}
div.stButton > button {
    background-color: #2E7D32;
    color:white;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL AND DATA
# --------------------------------------------------

model = joblib.load("yield_model.pkl")
df = pd.read_excel("Smart_Agriculture_Final_ML_Dataset (1).xlsx")
df = df.drop("ID", axis=1)

# --------------------------------------------------
# CSV FILE INIT
# --------------------------------------------------

HISTORY_FILE = "prediction_history.csv"

if not os.path.exists(HISTORY_FILE):
    pd.DataFrame(columns=[
        "Timestamp","State","Crop","Soil","Year",
        "Nitrogen","Phosphorus","Potassium",
        "Rainfall","Temperature","Humidity",
        "Irrigation","Area","Predicted_Yield","Total_Production"
    ]).to_csv(HISTORY_FILE, index=False)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🌾 AgriYield AI - Smart Crop Yield Predictor")

st.write("""
AI-powered platform to estimate **Crop Yield (kg/hectare)** using
soil nutrients, weather conditions, and farm parameters.
""")

# --------------------------------------------------
# SIDEBAR INPUTS
# --------------------------------------------------

st.sidebar.header("Farm Inputs")

state = st.sidebar.selectbox("State", sorted(df["State"].unique()))
crop = st.sidebar.selectbox("Crop", sorted(df["Crop"].unique()))
soil = st.sidebar.selectbox("Soil Type", sorted(df["Soil_Type"].unique()))

year = st.sidebar.number_input("Year", 2000, 2035, 2024)

# SMART DEFAULT NPK
use_auto = st.sidebar.checkbox("Use Recommended Values (Auto Fill)", value=True)

if use_auto:
    nitrogen = int(df["Nitrogen"].mean())
    phosphorus = int(df["Phosphorus"].mean())
    potassium = int(df["Potassium"].mean())
else:
    nitrogen = st.sidebar.slider("Nitrogen (kg/ha)", 0, 200, 60)
    phosphorus = st.sidebar.slider("Phosphorus (kg/ha)", 0, 200, 50)
    potassium = st.sidebar.slider("Potassium (kg/ha)", 0, 200, 40)

rainfall = st.sidebar.slider("Rainfall (mm)", 0, 1000, 120)
temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 25)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 60)

soil_ph = st.sidebar.slider("Soil pH", 3.0, 10.0, 6.5)
irrigation = st.sidebar.slider("Irrigation Coverage (%)", 0, 100, 70)
area = st.sidebar.number_input("Farm Area (hectares)", 0.1, 1000.0, 5.0)

# --------------------------------------------------
# CREATE INPUT DATA
# --------------------------------------------------

input_dict = {
    "Year": year,
    "State": state,
    "Crop": crop,
    "Soil_Type": soil,
    "Soil_pH": soil_ph,
    "Nitrogen": nitrogen,
    "Phosphorus": phosphorus,
    "Potassium": potassium,
    "Rainfall_mm": rainfall,
    "Temperature_C": temperature,
    "Humidity": humidity,
    "Irrigation_Coverage_%": irrigation,
    "Area_Hectare": area
}

input_df = pd.DataFrame([input_dict])
input_df = pd.get_dummies(input_df)
input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

prediction = model.predict(input_df)[0]
total_production = prediction * area

# --------------------------------------------------
# SAVE HISTORY (NO DUPLICATES FIX)
# --------------------------------------------------

def save_history(data):
    df_new = pd.DataFrame([data])
    df_new.to_csv(HISTORY_FILE, mode='a', header=False, index=False)

if "last_saved" not in st.session_state:
    st.session_state.last_saved = None

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if st.session_state.last_saved != current_time:
    history_data = {
        "Timestamp": current_time,
        "State": state,
        "Crop": crop,
        "Soil": soil,
        "Year": year,
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium,
        "Rainfall": rainfall,
        "Temperature": temperature,
        "Humidity": humidity,
        "Irrigation": irrigation,
        "Area": area,
        "Predicted_Yield": prediction,
        "Total_Production": total_production
    }

    save_history(history_data)
    st.session_state.last_saved = current_time

# --------------------------------------------------
# DISPLAY
# --------------------------------------------------

st.subheader("🌾 Yield Prediction")

c1, c2 = st.columns(2)

with c1:
    st.metric("Predicted Yield", f"{prediction:.2f} kg/hectare")

with c2:
    st.metric("Expected Total Production", f"{total_production:.2f} kg")

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

st.subheader("📊 Farm Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:
    nutrients = pd.DataFrame({
        "Nutrient": ["Nitrogen", "Phosphorus", "Potassium"],
        "Value": [nitrogen, phosphorus, potassium]
    })

    fig1 = px.bar(nutrients, x="Nutrient", y="Value", color="Nutrient",
                  title="Soil Nutrient Balance (kg/ha)")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        number={'suffix': " kg/ha"},
        title={'text': "Predicted Yield (kg/ha)"},
        gauge={'axis': {'range': [0, 7000]}}
    ))
    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# REAL HISTORY GRAPH
# --------------------------------------------------

st.subheader("📈 Prediction History")

history_df = pd.read_csv(HISTORY_FILE)

if len(history_df) > 1:
    history_df["Timestamp"] = pd.to_datetime(history_df["Timestamp"])
    history_df = history_df.sort_values("Timestamp")

    fig_hist = px.line(
        history_df,
        x="Timestamp",
        y="Predicted_Yield",
        title="Yield Trend (Real Data)",
        markers=True
    )

    fig_hist.update_layout(
        xaxis_title="Time",
        yaxis_title="Yield (kg/hectare)"
    )

    st.plotly_chart(fig_hist, use_container_width=True)
else:
    st.info("Not enough data yet")

# --------------------------------------------------
# PDF REPORT
# --------------------------------------------------

def generate_report():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200,10,"AgriYield AI Farm Report", ln=True)
    pdf.cell(200,10,f"State: {state}", ln=True)
    pdf.cell(200,10,f"Crop: {crop}", ln=True)
    pdf.cell(200,10,f"Soil: {soil}", ln=True)
    pdf.cell(200,10,f"Yield: {prediction:.2f}", ln=True)
    pdf.cell(200,10,f"Production: {total_production:.2f}", ln=True)

    file = "AgriYield_Report.pdf"
    pdf.output(file)
    return file

st.subheader("📄 Download Farm Report")

if st.button("Generate Report"):
    file = generate_report()
    with open(file, "rb") as f:
        st.download_button("Download Report", f, file_name=file)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")
st.write("AgriYield AI • Smart Agriculture Prediction Platform")
