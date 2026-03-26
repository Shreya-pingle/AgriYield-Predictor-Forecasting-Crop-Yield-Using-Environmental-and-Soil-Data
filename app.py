# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import plotly.express as px

# # ---------------------------
# # PAGE CONFIG
# # ---------------------------

# st.set_page_config(
#     page_title="Smart Agriculture Yield Predictor",
#     page_icon="🌾",
#     layout="wide"
# )

# # ---------------------------
# # LOAD MODEL
# # ---------------------------

# model = joblib.load("yield_model.pkl")

# # ---------------------------
# # LOAD DATASET
# # ---------------------------

# df = pd.read_excel("Smart_Agriculture_Final_ML_Dataset (1).xlsx")

# df = df.drop("ID", axis=1)

# # ---------------------------
# # TITLE
# # ---------------------------

# st.title("🌾 Smart Agriculture Yield Prediction System")

# st.markdown(
# """
# AI powered system to estimate **Crop Yield (kg/hectare)** based on environmental
# and soil parameters.
# """
# )

# # ---------------------------
# # SIDEBAR INPUTS
# # ---------------------------

# st.sidebar.header("Input Farm Data")

# rainfall = st.sidebar.slider("Rainfall (mm)", 0, 500, 100)

# temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 25)

# nitrogen = st.sidebar.slider("Nitrogen Level", 0, 150, 50)

# phosphorus = st.sidebar.slider("Phosphorus Level", 0, 150, 40)

# potassium = st.sidebar.slider("Potassium Level", 0, 150, 40)

# irrigation = st.sidebar.slider("Irrigation Coverage (%)", 0, 100, 60)

# # ---------------------------
# # CREATE INPUT DATAFRAME
# # ---------------------------

# input_data = pd.DataFrame({
#     "Rainfall_mm":[rainfall],
#     "Temperature_C":[temperature],
#     "Nitrogen":[nitrogen],
#     "Phosphorus":[phosphorus],
#     "Potassium":[potassium],
#     "Irrigation_Coverage_%":[irrigation]
# })

# # ---------------------------
# # PREDICTION
# # ---------------------------


# # Get model feature names
# model_features = model.feature_names_in_

# # Create full feature dataframe
# input_data = pd.DataFrame(columns=model_features)
# input_data.loc[0] = 0

# # Fill numeric values
# if "Rainfall_mm" in input_data.columns:
#     input_data["Rainfall_mm"] = rainfall

# if "Temperature_C" in input_data.columns:
#     input_data["Temperature_C"] = temperature

# if "Nitrogen" in input_data.columns:
#     input_data["Nitrogen"] = nitrogen

# if "Phosphorus" in input_data.columns:
#     input_data["Phosphorus"] = phosphorus

# if "Potassium" in input_data.columns:
#     input_data["Potassium"] = potassium

# if "Irrigation_Coverage_%" in input_data.columns:
#     input_data["Irrigation_Coverage_%"] = irrigation

# prediction = model.predict(input_data)[0]
# # ---------------------------
# # DISPLAY RESULT
# # ---------------------------

# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("🌱 Predicted Yield")

#     st.metric(
#         label="Estimated Yield (kg/hectare)",
#         value=f"{prediction:.2f}"
#     )

# with col2:

#     st.subheader("AI Recommendation")

#     suggestion = ""

#     if nitrogen < 40:
#         suggestion += "Increase Nitrogen fertilizer.\n"

#     if irrigation < 50:
#         suggestion += "Increase irrigation coverage.\n"

#     if rainfall < 80:
#         suggestion += "Low rainfall detected — irrigation required.\n"

#     if suggestion == "":
#         suggestion = "Optimal farming conditions detected."

#     st.success(suggestion)

# # ---------------------------
# # DATA VISUALIZATION
# # ---------------------------

# st.subheader("📊 Dataset Insights")

# col3, col4 = st.columns(2)

# with col3:

#     fig1 = px.histogram(
#         df,
#         x="Rainfall_mm",
#         title="Rainfall Distribution"
#     )

#     st.plotly_chart(fig1, use_container_width=True)

# with col4:

#     fig2 = px.scatter(
#         df,
#         x="Nitrogen",
#         y="Yield_kg_per_hectare",
#         title="Nitrogen vs Yield"
#     )

#     st.plotly_chart(fig2, use_container_width=True)

# # ---------------------------
# # CORRELATION HEATMAP
# # ---------------------------

# st.subheader("📉 Feature Correlation")

# corr = df.corr(numeric_only=True)

# fig3 = px.imshow(
#     corr,
#     text_auto=True,
#     aspect="auto",
#     color_continuous_scale="RdBu"
# )

# st.plotly_chart(fig3, use_container_width=True)

# # ---------------------------
# # FOOTER
# # ---------------------------

# st.markdown("---")
# st.markdown("Developed using AI & Machine Learning")



# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import plotly.express as px

# # -----------------------------
# # PAGE CONFIG
# # -----------------------------

# st.set_page_config(
#     page_title="Smart Agriculture Yield Predictor",
#     page_icon="🌾",
#     layout="wide"
#     st.markdown("""
# <style>

# .stApp {
#     background-color: #F4F8F2;
# }

# h1, h2, h3 {
#     color: #2E7D32;
# }

# .sidebar .sidebar-content {
#     background-color: #E8F5E9;
# }

# div.stButton > button {
#     background-color: #2E7D32;
#     color:white;
#     border-radius:10px;
# }

# </style>
# """, unsafe_allow_html=True)
# )

# # -----------------------------
# # LOAD MODEL + DATA
# # -----------------------------

# model = joblib.load("yield_model.pkl")

# df = pd.read_excel("Smart_Agriculture_Final_ML_Dataset (1).xlsx")

# df = df.drop("ID", axis=1)

# # -----------------------------
# # TITLE
# # -----------------------------

# st.title("🌾 Smart Agriculture Yield Prediction System")

# st.markdown(
# """
# AI powered platform to estimate **Crop Yield (kg/hectare)** using
# soil nutrients, weather conditions, and farm parameters.
# """
# )

# # -----------------------------
# # SIDEBAR INPUTS
# # -----------------------------

# st.sidebar.header("Farm Inputs")

# # Dropdown inputs

# state = st.sidebar.selectbox(
#     "State",
#     sorted(df["State"].unique())
# )

# crop = st.sidebar.selectbox(
#     "Crop",
#     sorted(df["Crop"].unique())
# )

# soil = st.sidebar.selectbox(
#     "Soil Type",
#     sorted(df["Soil_Type"].unique())
# )

# year = st.sidebar.number_input(
#     "Year",
#     2000,
#     2035,
#     2024
# )

# # Weather

# rainfall = st.sidebar.slider(
#     "Rainfall (mm)",
#     0,
#     500,
#     120
# )

# temperature = st.sidebar.slider(
#     "Temperature (°C)",
#     0,
#     50,
#     25
# )

# humidity = st.sidebar.slider(
#     "Humidity (%)",
#     0,
#     100,
#     60
# )

# # Soil nutrients

# nitrogen = st.sidebar.slider(
#     "Nitrogen (kg/ha)",
#     0,
#     200,
#     60
# )

# phosphorus = st.sidebar.slider(
#     "Phosphorus (kg/ha)",
#     0,
#     200,
#     50
# )

# potassium = st.sidebar.slider(
#     "Potassium (kg/ha)",
#     0,
#     200,
#     40
# )

# soil_ph = st.sidebar.slider(
#     "Soil pH",
#     3.0,
#     10.0,
#     6.5
# )

# # Farm management

# irrigation = st.sidebar.slider(
#     "Irrigation Coverage (%)",
#     0,
#     100,
#     70
# )

# area = st.sidebar.number_input(
#     "Farm Area (hectares)",
#     0.1,
#     1000.0,
#     5.0
# )

# # -----------------------------
# # CREATE INPUT DATAFRAME
# # -----------------------------

# input_dict = {
#     "Year": year,
#     "State": state,
#     "Crop": crop,
#     "Soil_Type": soil,
#     "Soil_pH": soil_ph,
#     "Nitrogen": nitrogen,
#     "Phosphorus": phosphorus,
#     "Potassium": potassium,
#     "Rainfall_mm": rainfall,
#     "Temperature_C": temperature,
#     "Humidity": humidity,
#     "Irrigation_Coverage_%": irrigation,
#     "Area_Hectare": area
# }

# input_df = pd.DataFrame([input_dict])

# # One hot encoding

# input_df = pd.get_dummies(input_df)

# # Align with model features

# input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

# # -----------------------------
# # PREDICTION
# # -----------------------------

# prediction = model.predict(input_df)[0]
# st.subheader("🌾 Yield Prediction")

# col1, col2 = st.columns(2)

# with col1:

#     st.metric(
#         "Predicted Yield",
#         f"{prediction:.2f} kg/hectare"
#     )

# with col2:

#     total_production = prediction * area

#     st.metric(
#         "Expected Total Production",
#         f"{total_production:.2f} kg"
#     )
# # -----------------------------
# # DISPLAY PREDICTION
# # -----------------------------

# st.subheader("🌱 Predicted Yield")

# col1, col2, col3 = st.columns(3)

# with col1:

#     st.metric(
#         "Yield (kg/hectare)",
#         f"{prediction:.2f}"
#     )

# with col2:

#     avg_yield = df["Yield_kg_per_hectare"].mean()

#     st.metric(
#         "Dataset Average Yield",
#         f"{avg_yield:.2f}"
#     )

# with col3:

#     difference = prediction - avg_yield

#     st.metric(
# #         "Difference vs Average",
# #         f"{difference:.2f}"
# #     )

# # # -----------------------------
# # # AI RECOMMENDATIONS
# # # -----------------------------

# # st.subheader("🤖 AI Farming Suggestions")

# # suggestions = []

# # if nitrogen < 40:
# #     suggestions.append("Increase Nitrogen fertilizer to improve yield.")

# # if phosphorus < 30:
# #     suggestions.append("Add Phosphorus fertilizer for better crop growth.")

# # if potassium < 30:
# #     suggestions.append("Potassium level is low — consider supplementation.")

# # if irrigation < 50:
# #     suggestions.append("Irrigation coverage is low — increase irrigation.")

# # if rainfall < 80:
# #     suggestions.append("Rainfall is low — irrigation support required.")

# # if soil_ph < 5.5:
# #     suggestions.append("Soil is too acidic — consider lime treatment.")

# # if soil_ph > 7.5:
# #     suggestions.append("Soil is alkaline — adjust pH with soil amendments.")

# # if len(suggestions) == 0:
# #     suggestions.append("Farm conditions look optimal for good yield.")

# # for s in suggestions:
# #     st.success(s)

# # # -----------------------------
# # # VISUALIZATION
# # # -----------------------------

# # st.subheader("📊 Agricultural Insights")

# # col4, col5 = st.columns(2)

# # with col4:

# #     fig1 = px.histogram(
# #         df,
# #         x="Yield_kg_per_hectare",
# #         title="Yield Distribution in Dataset"
# #     )

# #     st.plotly_chart(fig1, use_container_width=True)

# # with col5:

# #     fig2 = px.scatter(
# #         df,
# #         x="Rainfall_mm",
# #         y="Yield_kg_per_hectare",
# #         title="Rainfall vs Yield"
# #     )

# #     st.plotly_chart(fig2, use_container_width=True)

# # # -----------------------------
# # # FEATURE IMPORTANCE
# # # -----------------------------

# # st.subheader("📈 Feature Importance (Random Forest)")

# # importance = model.feature_importances_

# # features = model.feature_names_in_

# # imp_df = pd.DataFrame({
# #     "Feature": features,
# #     "Importance": importance
# # })

# # imp_df = imp_df.sort_values("Importance", ascending=False).head(10)

# # fig3 = px.bar(
# #     imp_df,
# #     x="Importance",
# #     y="Feature",
# #     orientation="h",
# #     title="Top Features Affecting Yield"
# # )

# # st.plotly_chart(fig3, use_container_width=True)

# # # -----------------------------
# # # FOOTER
# # # -----------------------------

# # st.markdown("---")

# # st.markdown(
# # "Smart Agriculture AI Dashboard • Built using Machine Learning and Streamlit"
# # )



# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import plotly.express as px
# from fpdf import FPDF

# # --------------------------------------------------
# # PAGE CONFIG
# # --------------------------------------------------

# st.set_page_config(
#     page_title="AgriYield AI Predictor",
#     page_icon="🌾",
#     layout="wide"
# )

# # --------------------------------------------------
# # THEME STYLE
# # --------------------------------------------------
# st.markdown("""
# <style>

# /* Main app background */
# .stApp {
#     background-color: #0E1117;
#     color: white;
# }

# /* Main text */
# p, span, label, div {
#     color: white;
# }

# /* Sidebar */
# section[data-testid="stSidebar"] {
#     background-color: #1B1F2A;
# }

# /* Sidebar text */
# section[data-testid="stSidebar"] p,
# section[data-testid="stSidebar"] span,
# section[data-testid="stSidebar"] label,
# section[data-testid="stSidebar"] div {
#     color: white !important;
# }

# /* Headers */
# h1, h2, h3 {
#     color: #E6E6E6;
# }

# /* Metric values */
# [data-testid="stMetricValue"] {
#     color: white;
#     font-size: 32px;
#     font-weight: bold;
# }

# /* Buttons */
# div.stButton > button {
#     background-color: #2E7D32;
#     color: white;
#     border-radius: 8px;
# }

# </style>
# """, unsafe_allow_html=True)
# # --------------------------------------------------
# # LOAD MODEL + DATA
# # --------------------------------------------------

# model = joblib.load("yield_model.pkl")

# df = pd.read_excel("Smart_Agriculture_Final_ML_Dataset (1).xlsx")

# df = df.drop("ID", axis=1)

# # --------------------------------------------------
# # TITLE
# # --------------------------------------------------

# st.title("🌾 AgriYield AI - Smart Crop Yield Predictor")

# st.write(
# """
# AI-powered platform to estimate **Crop Yield (kg/hectare)** using
# soil nutrients, weather conditions, and farm parameters.
# """
# )

# # --------------------------------------------------
# # SIDEBAR INPUTS
# # --------------------------------------------------

# st.sidebar.header("Farm Inputs")

# state = st.sidebar.selectbox("State", sorted(df["State"].unique()))
# crop = st.sidebar.selectbox("Crop", sorted(df["Crop"].unique()))
# soil = st.sidebar.selectbox("Soil Type", sorted(df["Soil_Type"].unique()))

# year = st.sidebar.number_input("Year", 2000, 2035, 2024)

# rainfall = st.sidebar.slider("Rainfall (mm)", 0, 500, 120)
# temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 25)
# humidity = st.sidebar.slider("Humidity (%)", 0, 100, 60)

# nitrogen = st.sidebar.slider("Nitrogen (kg/ha)", 0, 200, 60)
# phosphorus = st.sidebar.slider("Phosphorus (kg/ha)", 0, 200, 50)
# potassium = st.sidebar.slider("Potassium (kg/ha)", 0, 200, 40)

# soil_ph = st.sidebar.slider("Soil pH", 3.0, 10.0, 6.5)

# irrigation = st.sidebar.slider("Irrigation Coverage (%)", 0, 100, 70)

# area = st.sidebar.number_input("Farm Area (hectares)", 0.1, 1000.0, 5.0)

# # --------------------------------------------------
# # CREATE INPUT DATA
# # --------------------------------------------------

# input_dict = {
#     "Year": year,
#     "State": state,
#     "Crop": crop,
#     "Soil_Type": soil,
#     "Soil_pH": soil_ph,
#     "Nitrogen": nitrogen,
#     "Phosphorus": phosphorus,
#     "Potassium": potassium,
#     "Rainfall_mm": rainfall,
#     "Temperature_C": temperature,
#     "Humidity": humidity,
#     "Irrigation_Coverage_%": irrigation,
#     "Area_Hectare": area
# }

# input_df = pd.DataFrame([input_dict])

# input_df = pd.get_dummies(input_df)

# input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

# # --------------------------------------------------
# # PREDICTION
# # --------------------------------------------------

# prediction = model.predict(input_df)[0]

# st.subheader("🌾 Yield Prediction")

# col1, col2 = st.columns(2)

# with col1:
#     st.metric("Predicted Yield", f"{prediction:.2f} kg/hectare")

# with col2:
#     total_production = prediction * area
#     st.metric("Expected Total Production", f"{total_production:.2f} kg")

# # --------------------------------------------------
# # FARM HEALTH INDICATORS
# # --------------------------------------------------

# st.subheader("🌿 Farm Health Indicators")

# soil_health = (nitrogen + phosphorus + potassium) / 3
# water_health = (rainfall + irrigation) / 2
# weather_health = (temperature + humidity) / 2

# st.write("Soil Fertility")
# st.progress(min(int(soil_health),100))

# st.write("Water Availability")
# st.progress(min(int(water_health),100))

# st.write("Weather Suitability")
# st.progress(min(int(weather_health),100))

# # --------------------------------------------------
# # FERTILIZER OPTIMIZATION
# # --------------------------------------------------

# st.subheader("🧪 Fertilizer Optimization")

# if nitrogen < 40:
#     st.warning("Nitrogen level low — increase nitrogen fertilizer")

# if phosphorus < 30:
#     st.warning("Phosphorus level low — add phosphate fertilizer")

# if potassium < 30:
#     st.warning("Potassium low — use potash fertilizer")

# if nitrogen >=40 and phosphorus >=30 and potassium >=30:
#     st.success("Fertilizer levels are optimal")

# # --------------------------------------------------
# # YIELD IMPROVEMENT SUGGESTIONS
# # --------------------------------------------------

# st.subheader("📈 Yield Improvement Suggestions")

# if irrigation < 50:
#     st.info("Increase irrigation coverage")

# if rainfall < 80:
#     st.info("Low rainfall — irrigation recommended")

# if soil_ph < 5.5:
#     st.info("Soil acidic — apply lime")

# if soil_ph > 7.5:
#     st.info("Soil alkaline — adjust pH")

# # --------------------------------------------------
# # CHARTS
# # --------------------------------------------------

# st.subheader("📊 Agricultural Insights")

# col3, col4 = st.columns(2)

# with col3:

#     fig1 = px.scatter(
#         df,
#         x="Rainfall_mm",
#         y="Yield_kg_per_hectare",
#         color="Crop",
#         title="Rainfall Impact on Yield"
#     )

#     st.plotly_chart(fig1, use_container_width=True)

# with col4:

#     nutrients = pd.DataFrame({
#         "Nutrient":["Nitrogen","Phosphorus","Potassium"],
#         "Value":[nitrogen,phosphorus,potassium]
#     })

#     fig2 = px.bar(
#         nutrients,
#         x="Nutrient",
#         y="Value",
#         color="Nutrient",
#         title="Soil Nutrient Levels"
#     )

#     st.plotly_chart(fig2, use_container_width=True)

# # --------------------------------------------------
# # TEMPERATURE VS YIELD
# # --------------------------------------------------

# fig3 = px.scatter(
#     df,
#     x="Temperature_C",
#     y="Yield_kg_per_hectare",
#     color="Crop",
#     title="Temperature vs Yield"
# )

# st.plotly_chart(fig3, use_container_width=True)

# # --------------------------------------------------
# # INDIA STATE YIELD VISUALIZATION
# # --------------------------------------------------

# st.subheader("🇮🇳 Yield Analysis by State")

# state_yield = df.groupby("State")["Yield_kg_per_hectare"].mean().reset_index()

# fig_map = px.bar(
#     state_yield,
#     x="State",
#     y="Yield_kg_per_hectare",
#     color="Yield_kg_per_hectare",
#     title="Average Yield by State"
# )

# st.plotly_chart(fig_map, use_container_width=True)

# # --------------------------------------------------
# # PDF REPORT GENERATION
# # --------------------------------------------------

# def generate_report():

#     pdf = FPDF()

#     pdf.add_page()

#     pdf.set_font("Arial", size=12)

#     pdf.cell(200,10,"AgriYield AI Farm Report", ln=True)

#     pdf.cell(200,10,f"State: {state}", ln=True)
#     pdf.cell(200,10,f"Crop: {crop}", ln=True)
#     pdf.cell(200,10,f"Soil Type: {soil}", ln=True)

#     pdf.cell(200,10,f"Predicted Yield: {prediction:.2f} kg/hectare", ln=True)
#     pdf.cell(200,10,f"Expected Production: {total_production:.2f} kg", ln=True)

#     file_name = "AgriYield_Report.pdf"

#     pdf.output(file_name)

#     return file_name

# # --------------------------------------------------
# # DOWNLOAD REPORT
# # --------------------------------------------------

# st.subheader("📄 Download Farm Report")

# if st.button("Generate Report"):

#     file = generate_report()

#     with open(file, "rb") as f:

#         st.download_button(
#             label="Download Report",
#             data=f,
#             file_name="AgriYield_Report.pdf",
#             mime="application/pdf"
#         )

# # --------------------------------------------------
# # FOOTER
# # --------------------------------------------------

# st.markdown("---")

# st.write("AgriYield AI • Smart Agriculture Prediction Platform")




# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import plotly.express as px
# import plotly.graph_objects as go
# from fpdf import FPDF

# # --------------------------------------------------
# # PAGE CONFIG
# # --------------------------------------------------

# st.set_page_config(
#     page_title="AgriYield AI Predictor",
#     page_icon="🌾",
#     layout="wide"
# )

# # --------------------------------------------------
# # UI THEME
# # --------------------------------------------------
# st.markdown("""
# <style>

# /* App background */
# .stApp {
#     background-color: #F4F8F2;
# }

# /* Main text */
# p, span, label {
#     color: #1B4332 !important;
# }

# /* Titles */
# h1, h2, h3 {
#     color: #1B4332 !important;
# }

# /* Metrics */
# [data-testid="stMetricValue"] {
#     color: #1B4332;
#     font-size: 32px;
#     font-weight: bold;
# }

# /* Sidebar */
# section[data-testid="stSidebar"] {
#     background-color: #E8F5E9;
# }

# /* Buttons */
# div.stButton > button {
#     background-color: #2E7D32;
#     color:white;
#     border-radius:8px;
# }

# </style>
# """, unsafe_allow_html=True)

# # --------------------------------------------------
# # LOAD MODEL AND DATA
# # --------------------------------------------------

# model = joblib.load("yield_model.pkl")

# df = pd.read_excel("Smart_Agriculture_Final_ML_Dataset (1).xlsx")

# df = df.drop("ID", axis=1)

# # --------------------------------------------------
# # TITLE
# # --------------------------------------------------

# st.title("🌾 AgriYield AI - Smart Crop Yield Predictor")

# st.write(
# """
# AI-powered platform to estimate **Crop Yield (kg/hectare)** using
# soil nutrients, weather conditions, and farm parameters.
# """
# )

# # --------------------------------------------------
# # SIDEBAR INPUTS
# # --------------------------------------------------

# st.sidebar.header("Farm Inputs")

# state = st.sidebar.selectbox("State", sorted(df["State"].unique()))
# crop = st.sidebar.selectbox("Crop", sorted(df["Crop"].unique()))
# soil = st.sidebar.selectbox("Soil Type", sorted(df["Soil_Type"].unique()))

# year = st.sidebar.number_input("Year", 2000, 2035, 2024)

# rainfall = st.sidebar.slider("Rainfall (mm)", 0, 500, 120)
# temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 25)
# humidity = st.sidebar.slider("Humidity (%)", 0, 100, 60)

# nitrogen = st.sidebar.slider("Nitrogen (kg/ha)", 0, 200, 60)
# phosphorus = st.sidebar.slider("Phosphorus (kg/ha)", 0, 200, 50)
# potassium = st.sidebar.slider("Potassium (kg/ha)", 0, 200, 40)

# soil_ph = st.sidebar.slider("Soil pH", 3.0, 10.0, 6.5)

# irrigation = st.sidebar.slider("Irrigation Coverage (%)", 0, 100, 70)

# area = st.sidebar.number_input("Farm Area (hectares)", 0.1, 1000.0, 5.0)

# # --------------------------------------------------
# # CREATE INPUT DATA
# # --------------------------------------------------

# input_dict = {
#     "Year": year,
#     "State": state,
#     "Crop": crop,
#     "Soil_Type": soil,
#     "Soil_pH": soil_ph,
#     "Nitrogen": nitrogen,
#     "Phosphorus": phosphorus,
#     "Potassium": potassium,
#     "Rainfall_mm": rainfall,
#     "Temperature_C": temperature,
#     "Humidity": humidity,
#     "Irrigation_Coverage_%": irrigation,
#     "Area_Hectare": area
# }

# input_df = pd.DataFrame([input_dict])

# input_df = pd.get_dummies(input_df)

# input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

# # --------------------------------------------------
# # PREDICTION
# # --------------------------------------------------

# prediction = model.predict(input_df)[0]

# total_production = prediction * area

# st.subheader("🌾 Yield Prediction")

# col1, col2 = st.columns(2)

# with col1:
#     st.metric("Predicted Yield", f"{prediction:.2f} kg/hectare")

# with col2:
#     st.metric("Expected Total Production", f"{total_production:.2f} kg")

# # --------------------------------------------------
# # FARM HEALTH INDICATORS
# # --------------------------------------------------
# # --------------------------------------------------
# # FARM HEALTH INDICATORS
# # --------------------------------------------------

# st.subheader("🌿 Farm Health Indicators")

# soil_health = min(int((nitrogen + phosphorus + potassium) / 3), 100)
# water_health = min(int((rainfall + irrigation) / 2), 100)
# weather_health = min(int((temperature + humidity) / 2), 100)

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("Soil Fertility", f"{soil_health}%")
#     st.progress(soil_health)

# with col2:
#     st.metric("Water Availability", f"{water_health}%")
#     st.progress(water_health)

# with col3:
#     st.metric("Weather Suitability", f"{weather_health}%")
#     st.progress(weather_health)

# # --------------------------------------------------
# # FERTILIZER OPTIMIZATION
# # --------------------------------------------------

# st.subheader("🧪 Fertilizer Optimization")

# if nitrogen < 40:
#     st.warning("Nitrogen level low — increase nitrogen fertilizer")

# if phosphorus < 30:
#     st.warning("Phosphorus level low — add phosphate fertilizer")

# if potassium < 30:
#     st.warning("Potassium low — use potash fertilizer")

# if nitrogen >=40 and phosphorus >=30 and potassium >=30:
#     st.success("Fertilizer levels are optimal")

# # --------------------------------------------------
# # YIELD IMPROVEMENT SUGGESTIONS
# # --------------------------------------------------

# st.subheader("📈 Yield Improvement Suggestions")

# if irrigation < 50:
#     st.info("Increase irrigation coverage")

# if rainfall < 80:
#     st.info("Low rainfall — irrigation recommended")

# if soil_ph < 5.5:
#     st.info("Soil acidic — apply lime")

# if soil_ph > 7.5:
#     st.info("Soil alkaline — adjust pH")

# # --------------------------------------------------
# # FARM ANALYTICS DASHBOARD
# # --------------------------------------------------
# # --------------------------------------------------
# # FARM ANALYTICS DASHBOARD
# # --------------------------------------------------

# st.subheader("📊 Farm Analytics Dashboard")

# col1, col2 = st.columns(2)

# # -------------------------------
# # Soil Nutrient Balance Chart
# # -------------------------------

# with col1:

#     nutrients = pd.DataFrame({
#         "Nutrient": ["Nitrogen", "Phosphorus", "Potassium"],
#         "Value": [nitrogen, phosphorus, potassium]
#     })

#     fig1 = px.bar(
#         nutrients,
#         x="Nutrient",
#         y="Value",
#         color="Nutrient",
#         title="Soil Nutrient Balance (kg/ha)",
#         labels={
#             "Value": "Nutrient Level (kg/ha)",
#             "Nutrient": "Soil Nutrient"
#         }
#     )

#     st.plotly_chart(fig1, use_container_width=True)


# # -------------------------------
# # Yield Potential Gauge
# # -------------------------------

# # Yield Potential Gauge
# with col2:

#     fig2 = go.Figure(go.Indicator(
#         mode="gauge+number",
#         value=prediction,
#         number={'suffix': " kg/ha"},
#         title={'text': "Predicted Yield Potential (kg/ha)"},
#         gauge={
#             'axis': {'range': [0, 7000]},
#             'bar': {'color': "green"},
#             'steps': [
#                 {'range': [0, 2500], 'color': "#ffcccc"},
#                 {'range': [2500, 4500], 'color': "#fff2cc"},
#                 {'range': [4500, 7000], 'color': "#ccffcc"}
#             ]
#         }
#     ))

#     st.plotly_chart(fig2, use_container_width=True)

# # --------------------------------------------------
# # PDF REPORT
# # --------------------------------------------------

# def generate_report():

#     pdf = FPDF()
#     pdf.add_page()

#     pdf.set_font("Arial", size=12)

#     pdf.cell(200,10,"AgriYield AI Farm Report", ln=True)

#     pdf.cell(200,10,f"State: {state}", ln=True)
#     pdf.cell(200,10,f"Crop: {crop}", ln=True)
#     pdf.cell(200,10,f"Soil Type: {soil}", ln=True)

#     pdf.cell(200,10,f"Predicted Yield: {prediction:.2f} kg/hectare", ln=True)
#     pdf.cell(200,10,f"Expected Production: {total_production:.2f} kg", ln=True)

#     file_name = "AgriYield_Report.pdf"

#     pdf.output(file_name)

#     return file_name

# # --------------------------------------------------
# # DOWNLOAD REPORT
# # --------------------------------------------------

# st.subheader("📄 Download Farm Report")

# if st.button("Generate Report"):

#     file = generate_report()

#     with open(file, "rb") as f:

#         st.download_button(
#             label="Download Report",
#             data=f,
#             file_name="AgriYield_Report.pdf",
#             mime="application/pdf"
#         )

# # --------------------------------------------------
# # FOOTER
# # --------------------------------------------------

# st.markdown("---")

# st.write("AgriYield AI • Smart Agriculture Prediction Platform")



# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import plotly.express as px
# import plotly.graph_objects as go
# from fpdf import FPDF
# import os
# from datetime import datetime

# # --------------------------------------------------
# # PAGE CONFIG
# # --------------------------------------------------

# st.set_page_config(
#     page_title="AgriYield AI Predictor",
#     page_icon="🌾",
#     layout="wide"
# )

# # --------------------------------------------------
# # UI THEME
# # --------------------------------------------------

# st.markdown("""
# <style>
# .stApp { background-color: #F4F8F2; }
# p, span, label { color: #1B4332 !important; }
# h1, h2, h3 { color: #1B4332 !important; }
# [data-testid="stMetricValue"] {
#     color: #1B4332;
#     font-size: 32px;
#     font-weight: bold;
# }
# section[data-testid="stSidebar"] {
#     background-color: #E8F5E9;
# }
# div.stButton > button {
#     background-color: #2E7D32;
#     color:white;
#     border-radius:8px;
# }
# </style>
# """, unsafe_allow_html=True)

# # --------------------------------------------------
# # LOAD MODEL AND DATA
# # --------------------------------------------------

# model = joblib.load("yield_model.pkl")
# df = pd.read_excel("Smart_Agriculture_Final_ML_Dataset (1).xlsx")
# df = df.drop("ID", axis=1)

# # --------------------------------------------------
# # TITLE
# # --------------------------------------------------

# st.title("🌾 AgriYield AI - Smart Crop Yield Predictor")

# st.write("""
# AI-powered platform to estimate **Crop Yield (kg/hectare)** using
# soil nutrients, weather conditions, and farm parameters.
# """)

# # --------------------------------------------------
# # SIDEBAR INPUTS
# # --------------------------------------------------

# st.sidebar.header("Farm Inputs")

# state = st.sidebar.selectbox("State", sorted(df["State"].unique()))
# crop = st.sidebar.selectbox("Crop", sorted(df["Crop"].unique()))
# soil = st.sidebar.selectbox("Soil Type", sorted(df["Soil_Type"].unique()))

# year = st.sidebar.number_input("Year", 2000, 2035, 2024)

# # AUTO DEFAULT OPTION
# use_defaults = st.sidebar.checkbox("Use Recommended Values (Auto Fill)", value=True)

# if use_defaults:
#     rainfall = int(df["Rainfall_mm"].mean())
#     temperature = int(df["Temperature_C"].mean())
#     humidity = int(df["Humidity"].mean())
#     nitrogen = int(df["Nitrogen"].mean())
#     phosphorus = int(df["Phosphorus"].mean())
#     potassium = int(df["Potassium"].mean())
# else:
#     rainfall = st.sidebar.slider("Rainfall (mm)", 0, 500, 120)
#     temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 25)
#     humidity = st.sidebar.slider("Humidity (%)", 0, 100, 60)
#     nitrogen = st.sidebar.slider("Nitrogen (kg/ha)", 0, 200, 60)
#     phosphorus = st.sidebar.slider("Phosphorus (kg/ha)", 0, 200, 50)
#     potassium = st.sidebar.slider("Potassium (kg/ha)", 0, 200, 40)

# soil_ph = st.sidebar.slider("Soil pH", 3.0, 10.0, 6.5)
# irrigation = st.sidebar.slider("Irrigation Coverage (%)", 0, 100, 70)
# area = st.sidebar.number_input("Farm Area (hectares)", 0.1, 1000.0, 5.0)

# # --------------------------------------------------
# # CREATE INPUT DATA
# # --------------------------------------------------

# input_dict = {
#     "Year": year,
#     "State": state,
#     "Crop": crop,
#     "Soil_Type": soil,
#     "Soil_pH": soil_ph,
#     "Nitrogen": nitrogen,
#     "Phosphorus": phosphorus,
#     "Potassium": potassium,
#     "Rainfall_mm": rainfall,
#     "Temperature_C": temperature,
#     "Humidity": humidity,
#     "Irrigation_Coverage_%": irrigation,
#     "Area_Hectare": area
# }

# input_df = pd.DataFrame([input_dict])
# input_df = pd.get_dummies(input_df)
# input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

# # --------------------------------------------------
# # PREDICTION
# # --------------------------------------------------

# prediction = model.predict(input_df)[0]
# total_production = prediction * area

# # --------------------------------------------------
# # SAVE HISTORY (UPDATED)
# # --------------------------------------------------

# HISTORY_FILE = "prediction_history.csv"

# new_entry = pd.DataFrame([{
#     "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     "State": state,
#     "Crop": crop,
#     "Soil": soil,
#     "Year": year,
#     "Nitrogen": nitrogen,
#     "Phosphorus": phosphorus,
#     "Potassium": potassium,
#     "Rainfall": rainfall,
#     "Temperature": temperature,
#     "Humidity": humidity,
#     "Irrigation": irrigation,
#     "Area": area,
#     "Predicted_Yield": prediction
# }])

# if os.path.exists(HISTORY_FILE):
#     new_entry.to_csv(HISTORY_FILE, mode='a', header=False, index=False)
# else:
#     new_entry.to_csv(HISTORY_FILE, index=False)

# # --------------------------------------------------
# # DISPLAY
# # --------------------------------------------------

# st.subheader("🌾 Yield Prediction")

# col1, col2 = st.columns(2)

# with col1:
#     st.metric("Predicted Yield", f"{prediction:.2f} kg/hectare")

# with col2:
#     st.metric("Expected Total Production", f"{total_production:.2f} kg")

# # --------------------------------------------------
# # FARM HEALTH
# # --------------------------------------------------

# st.subheader("🌿 Farm Health Indicators")

# soil_health = min(int((nitrogen + phosphorus + potassium) / 3), 100)
# water_health = min(int((rainfall + irrigation) / 2), 100)
# weather_health = min(int((temperature + humidity) / 2), 100)

# c1, c2, c3 = st.columns(3)

# with c1:
#     st.metric("Soil Fertility", f"{soil_health}%")
#     st.progress(soil_health)

# with c2:
#     st.metric("Water Availability", f"{water_health}%")
#     st.progress(water_health)

# with c3:
#     st.metric("Weather Suitability", f"{weather_health}%")
#     st.progress(weather_health)

# # --------------------------------------------------
# # SUGGESTIONS
# # --------------------------------------------------

# st.subheader("🧪 Fertilizer Optimization")

# if nitrogen < 40:
#     st.warning("Nitrogen low — increase fertilizer")
# if phosphorus < 30:
#     st.warning("Phosphorus low — add fertilizer")
# if potassium < 30:
#     st.warning("Potassium low — add fertilizer")
# if nitrogen >= 40 and phosphorus >= 30 and potassium >= 30:
#     st.success("Fertilizer levels are optimal")

# # --------------------------------------------------
# # DASHBOARD
# # --------------------------------------------------

# st.subheader("📊 Farm Analytics Dashboard")

# col1, col2 = st.columns(2)

# with col1:
#     nutrients = pd.DataFrame({
#         "Nutrient": ["Nitrogen", "Phosphorus", "Potassium"],
#         "Value": [nitrogen, phosphorus, potassium]
#     })

#     fig1 = px.bar(
#         nutrients,
#         x="Nutrient",
#         y="Value",
#         color="Nutrient",
#         title="Soil Nutrient Balance (kg/ha)"
#     )
#     st.plotly_chart(fig1, use_container_width=True)

# with col2:
#     fig2 = go.Figure(go.Indicator(
#         mode="gauge+number",
#         value=prediction,
#         number={'suffix': " kg/ha"},
#         title={'text': "Predicted Yield (kg/ha)"},
#         gauge={
#             'axis': {'range': [0, 7000]},
#             'bar': {'color': "green"},
#             'steps': [
#                 {'range': [0, 2500], 'color': "#ffcccc"},
#                 {'range': [2500, 4500], 'color': "#fff2cc"},
#                 {'range': [4500, 7000], 'color': "#ccffcc"}
#             ]
#         }
#     ))
#     st.plotly_chart(fig2, use_container_width=True)

# # --------------------------------------------------
# # HISTORY GRAPH (FIXED)
# # --------------------------------------------------

# st.subheader("📈 Prediction History")

# if os.path.exists(HISTORY_FILE):
#     hist_df = pd.read_csv(HISTORY_FILE)

#     if len(hist_df) > 1:
#         fig_hist = px.line(
#             hist_df,
#             x="Timestamp",
#             y="Predicted_Yield",
#             title="Yield Trend (Real Data)",
#             markers=True
#         )

#         fig_hist.update_layout(
#             xaxis_title="Time",
#             yaxis_title="Yield (kg/ha)"
#         )

#         st.plotly_chart(fig_hist, use_container_width=True)
#     else:
#         st.info("Not enough history yet")

# # --------------------------------------------------
# # PDF REPORT
# # --------------------------------------------------

# def generate_report():
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.cell(200,10,"AgriYield AI Farm Report", ln=True)
#     pdf.cell(200,10,f"State: {state}", ln=True)
#     pdf.cell(200,10,f"Crop: {crop}", ln=True)
#     pdf.cell(200,10,f"Soil Type: {soil}", ln=True)
#     pdf.cell(200,10,f"Predicted Yield: {prediction:.2f}", ln=True)
#     pdf.cell(200,10,f"Total Production: {total_production:.2f}", ln=True)

#     file = "AgriYield_Report.pdf"
#     pdf.output(file)
#     return file

# st.subheader("📄 Download Farm Report")

# if st.button("Generate Report"):
#     file = generate_report()
#     with open(file, "rb") as f:
#         st.download_button(
#             label="Download Report",
#             data=f,
#             file_name=file,
#             mime="application/pdf"
#         )

# # --------------------------------------------------
# # FOOTER
# # --------------------------------------------------

# st.markdown("---")
# st.write("AgriYield AI • Smart Agriculture Prediction Platform")




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