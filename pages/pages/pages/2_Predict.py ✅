import streamlit as st
import pandas as pd
import joblib

model = joblib.load("attrition_model.pkl")

st.title("🤖 Attrition Predictor")

age = st.number_input("Age", 18, 60)
salary = st.number_input("Salary", 10000, 200000)
years = st.number_input("Years", 0, 40)
overtime = st.selectbox("Overtime", [0, 1])
satisfaction = st.slider("Satisfaction", 1, 5)

if st.button("Predict"):
    input_data = pd.DataFrame([[age, salary, years, overtime, satisfaction]],
                              columns=['age','salary','years_at_company','overtime','job_satisfaction'])

    pred = model.predict(input_data)
    prob = model.predict_proba(input_data)

    confidence = prob[0][pred[0]] * 100

    if pred[0] == 1:
        st.error(f"⚠️ High Risk ({confidence:.2f}%)")
    else:
        st.success(f"✅ Low Risk ({confidence:.2f}%)")
