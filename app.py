import streamlit as st
import pandas as pd
import joblib

# ===== CONFIG =====
st.set_page_config(page_title="HR AI System", layout="wide")

# ===== LOAD MODEL =====
model = joblib.load("attrition_model.pkl")

# ===== PREMIUM CSS =====
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}
.title {
    font-size: 42px;
    font-weight: bold;
}
.card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
}
.stButton>button {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("<div class='title'>💼 HR AI System</div>", unsafe_allow_html=True)
st.caption("AI-powered employee attrition analysis")

st.write("---")

# ===== NAVIGATION =====
page = st.radio("", ["Dashboard", "Predict", "Resume", "About"], horizontal=True)

# =========================
# 📊 DASHBOARD (CONNECTED TO MODEL)
# =========================
if page == "Dashboard":
    st.markdown("## 📊 HR Dashboard (AI Insights)")

    sample_data = pd.DataFrame({
        "age": [25, 30, 45, 22, 35],
        "salary": [30000, 50000, 80000, 25000, 60000],
        "years_at_company": [2, 5, 10, 1, 7],
        "overtime": [0, 1, 1, 0, 1],
        "job_satisfaction": [3, 4, 2, 5, 3]
    })

    predictions = model.predict(sample_data)
    sample_data["Prediction"] = predictions

    total = len(sample_data)
    high_risk = sum(predictions)
    low_risk = total - high_risk

    col1, col2, col3 = st.columns(3)

    col1.markdown(f"<div class='card'><h3>Total Employees</h3><h1>{total}</h1></div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='card'><h3>High Risk</h3><h1>{high_risk}</h1></div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='card'><h3>Low Risk</h3><h1>{low_risk}</h1></div>", unsafe_allow_html=True)

    st.write("")

    st.markdown("### 📊 Risk Distribution")
    chart_data = pd.DataFrame({
        "Category": ["High Risk", "Low Risk"],
        "Count": [high_risk, low_risk]
    })
    st.bar_chart(chart_data.set_index("Category"))

    st.write("")
    st.markdown("### 📋 Data Preview")
    st.dataframe(sample_data)

# =========================
# 🤖 PREDICT
# =========================
elif page == "Predict":
    st.markdown("## 🤖 Attrition Predictor")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 60)
        salary = st.number_input("Salary", 10000, 200000)
        years = st.number_input("Years at Company", 0, 40)

    with col2:
        overtime = st.selectbox("Overtime", ["No", "Yes"])
        satisfaction = st.slider("Job Satisfaction", 1, 5)

    if st.button("Predict 🚀"):
        overtime_val = 1 if overtime == "Yes" else 0

        input_data = pd.DataFrame([[age, salary, years, overtime_val, satisfaction]],
            columns=['age','salary','years_at_company','overtime','job_satisfaction'])

        pred = model.predict(input_data)

        if pred[0] == 1:
            st.error("⚠️ High Risk of Attrition")
        else:
            st.success("✅ Low Risk of Attrition")

# =========================
# 📄 RESUME (SMART SCORING)
# =========================
elif page == "Resume":
    st.markdown("## 📄 Resume Screening (AI Powered)")

    file = st.file_uploader("Upload Resume (.txt)", type=["txt"])

    role = st.selectbox("Select Job Role", ["Data Analyst", "ML Engineer", "HR"])

    role_skills = {
        "Data Analyst": ["python", "sql", "excel", "power bi"],
        "ML Engineer": ["python", "machine learning", "deep learning", "tensorflow"],
        "HR": ["communication", "management", "recruitment"]
    }

    if file:
        text = file.read().decode("utf-8").lower()

        skills_needed = role_skills[role]
        found_skills = [s for s in skills_needed if s in text]

        score = int((len(found_skills) / len(skills_needed)) * 100)

        st.markdown("### 🔍 Analysis Result")
        st.write("**Skills Found:**", found_skills)
        st.write(f"**Score:** {score}%")

        if score >= 70:
            st.success("✅ Good Candidate")
        elif score >= 40:
            st.warning("⚠️ Average Candidate")
        else:
            st.error("❌ Not Suitable")

# =========================
# 📘 ABOUT
# =========================
elif page == "About":
    st.markdown("## 📘 About")

    st.markdown("""
<div class='card'>
<h3>About This Project</h3>
<p>
This AI-powered HR system helps companies:
<ul>
<li>Predict employee attrition</li>
<li>Analyze workforce trends</li>
<li>Screen resumes intelligently</li>
</ul>
</p>
</div>
""", unsafe_allow_html=True)
