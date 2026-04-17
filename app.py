import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="Smart HR AI System", layout="wide")

# Load model
model = joblib.load("attrition_model.pkl")

# Custom CSS (Premium UI)
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1 {
    color: #00FFAA;
    text-align: center;
}
h3 {
    color: #FFFFFF;
}
.stButton>button {
    background-color: #00FFAA;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔧 Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "About Project"])

# ===========================
# ABOUT PAGE
# ===========================
if page == "About Project":
    st.title("📘 About This Project")
    st.write("""
    This Smart HR AI System predicts employee attrition using Machine Learning.
    
    🔹 Model Used: Random Forest  
    🔹 Features: Age, Salary, Overtime, Satisfaction, Experience  
    🔹 Output: Attrition Risk (High / Low)
    
    This helps companies take proactive decisions to retain employees.
    """)

# ===========================
# HOME PAGE
# ===========================
else:
    st.title("💼 Smart HR AI System")
    st.markdown("### Predict Employee Attrition with AI")

    st.markdown("""
    ---
    ### 🚀 Features:
    - AI-based Attrition Prediction  
    - Real-time Input Processing  
    - Interactive Dashboard  
    ---
    """)

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Employee Details")

        age = st.number_input("Age", 18, 60)
        salary = st.number_input("Salary", 10000, 200000)
        years = st.number_input("Years at Company", 0, 40)
        overtime = st.selectbox("Overtime", [0, 1])
        satisfaction = st.slider("Job Satisfaction", 1, 5)

    with col2:
        st.subheader("🤖 Prediction Result")

        if st.button("Predict"):
            input_data = pd.DataFrame([[age, salary, years, overtime, satisfaction]],
                                      columns=['age', 'salary', 'years_at_company', 'overtime', 'job_satisfaction'])

            prediction = model.predict(input_data)
            prob = model.predict_proba(input_data)

            if prediction[0] == 1:
                st.error("⚠️ High Risk of Attrition")
            else:
                st.success("✅ Low Risk of Attrition")

            st.write("### 🔍 Model Confidence")
            st.write(prob)
