
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("attrition_model.pkl")

st.title("Employee Attrition Predictor")

# Inputs
age = st.number_input("Age", min_value=18, max_value=60)
salary = st.number_input("Salary", min_value=10000, max_value=200000)
years = st.number_input("Years at Company", min_value=0, max_value=40)
overtime = st.selectbox("Overtime", [0, 1])
satisfaction = st.slider("Job Satisfaction", 1, 5)

# Prediction
if st.button("Predict"):
    input_data = pd.DataFrame([[age, salary, years, overtime, satisfaction]],
                              columns=['age', 'salary', 'years_at_company', 'overtime', 'job_satisfaction'])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Attrition")
    else:
        st.success("✅ Low Risk of Attrition")
