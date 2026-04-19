import streamlit as st
st.set_page_config(page_title="Predict Attrition", layout="wide")

import pandas as pd
import joblib

model = joblib.load("attrition_model.pkl")

st.title("🤖 Attrition Predictor")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Employee Details")

    age = st.number_input("Age", 18, 60)
    salary = st.number_input("Salary", 10000, 200000)
    years = st.number_input("Years at Company", 0, 40)
    overtime = st.selectbox("Overtime", ["No", "Yes"])
    satisfaction = st.slider("Job Satisfaction", 1, 5)

with col2:
    st.subheader("📊 Result")

    if st.button("Predict 🚀"):

        overtime_val = 1 if overtime == "Yes" else 0

        input_data = pd.DataFrame([[age, salary, years, overtime_val, satisfaction]],
                                  columns=['age','salary','years_at_company','overtime','job_satisfaction'])

        pred = model.predict(input_data)
        prob = model.predict_proba(input_data)

        confidence = prob[0][pred[0]] * 100

        if pred[0] == 1:
            st.error(f"⚠️ High Risk of Attrition ({confidence:.2f}%)")
            st.write("💡 Suggestions:")
            st.write("- Improve job satisfaction")
            st.write("- Reduce overtime")
            st.write("- Offer incentives")

        else:
            st.success(f"✅ Low Risk of Attrition ({confidence:.2f}%)")
            st.write("👍 Employee is stable")
