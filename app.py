import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="HR AI System", layout="wide")

model = joblib.load("attrition_model.pkl")

# ===== HEADER =====
st.title("💼 HR AI System")

page = st.radio(
    "",
    ["Dashboard", "Predict", "Resume", "About"],
    horizontal=True
)

# ===== DASHBOARD =====
if page == "Dashboard":
    st.subheader("📊 HR Dashboard")
    st.write("Basic analytics here")

# ===== PREDICT =====
elif page == "Predict":
    st.subheader("🤖 Attrition Predictor")

    age = st.number_input("Age", 18, 60)
    salary = st.number_input("Salary", 10000, 200000)

    if st.button("Predict"):
        st.success("Prediction working")

# ===== RESUME =====
elif page == "Resume":
    st.subheader("📄 Resume Screening")
    file = st.file_uploader("Upload resume")

# ===== ABOUT =====
elif page == "About":
    st.subheader("📘 About")
    st.write("HR AI System project")
