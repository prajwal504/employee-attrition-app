import streamlit as st
import pandas as pd
import joblib

# ===== PAGE CONFIG =====
st.set_page_config(page_title="HR AI System", layout="wide")

# ===== LOAD MODEL =====
model = joblib.load("attrition_model.pkl")

# ===== CUSTOM CSS (LIGHT WEBSITE STYLE) =====
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}

h1 {
    color: #2c3e50;
    text-align: center;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.stButton>button {
    background-color: #3498db;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

.result-box {
    padding: 15px;
    border-radius: 10px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("<h1>💼 HR AI Employee Attrition System</h1>", unsafe_allow_html=True)

st.markdown("""
<center>
Predict employee attrition using AI and make better HR decisions.
</center>
""", unsafe_allow_html=True)

st.write("")

# ===== MAIN LAYOUT =====
col1, col2 = st.columns([1,1])

# ===== INPUT CARD =====
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 Employee Details")

    age = st.number_input("Age", 18, 60)
    salary = st.number_input("Salary", 10000, 200000)
    years = st.number_input("Years at Company", 0, 40)
    overtime = st.selectbox("Overtime", ["No", "Yes"])
    satisfaction = st.slider("Job Satisfaction", 1, 5)

    st.markdown('</div>', unsafe_allow_html=True)

# ===== OUTPUT CARD =====
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🤖 Prediction Result")

    if st.button("Predict Attrition"):

        overtime_val = 1 if overtime == "Yes" else 0

        input_data = pd.DataFrame([[age, salary, years, overtime_val, satisfaction]],
                                  columns=['age','salary','years_at_company','overtime','job_satisfaction'])

        pred = model.predict(input_data)
        prob = model.predict_proba(input_data)

        confidence = prob[0][pred[0]] * 100

        if pred[0] == 1:
            st.markdown(f"""
            <div class="result-box" style="background:#ffe6e6; color:#c0392b;">
            ⚠️ High Risk of Attrition<br>
            Confidence: {confidence:.2f}%
            </div>
            """, unsafe_allow_html=True)

            st.write("### 💡 Recommendations")
            st.write("- Improve job satisfaction")
            st.write("- Reduce overtime workload")
            st.write("- Offer better incentives")

        else:
            st.markdown(f"""
            <div class="result-box" style="background:#e8f8f5; color:#27ae60;">
            ✅ Low Risk of Attrition<br>
            Confidence: {confidence:.2f}%
            </div>
            """, unsafe_allow_html=True)

            st.write("### 👍 Status")
            st.write("- Employee is stable")
            st.write("- Maintain current environment")

    st.markdown('</div>', unsafe_allow_html=True)

# ===== FOOTER =====
st.write("---")
st.markdown("""
<center>
© 2026 HR AI System | Built with Machine Learning & Streamlit
</center>
""", unsafe_allow_html=True)
