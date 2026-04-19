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

/* Background */
.main {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: bold;
}

/* Card */
.card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
}

/* Button */
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
page = st.radio(
    "",
    ["Dashboard", "Predict", "Resume", "About"],
    horizontal=True
)

st.write("")

# =========================
# 📊 DASHBOARD
# =========================
if page == "Dashboard":
    st.markdown("## 📊 HR Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.markdown("<div class='card'><h3>Employees</h3><h1>58</h1></div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'><h3>Attrition Rate</h3><h1>12%</h1></div>", unsafe_allow_html=True)
    col3.markdown("<div class='card'><h3>Satisfaction</h3><h1>3.8/5</h1></div>", unsafe_allow_html=True)

    st.write("")

    data = pd.DataFrame({
        "Department": ["HR", "IT", "Sales", "Finance"],
        "Employees": [10, 25, 15, 8]
    })

    st.markdown("### 📈 Department Overview")
    st.bar_chart(data.set_index("Department"))

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

    st.write("")

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
# 📄 RESUME
# =========================
elif page == "Resume":
    st.markdown("## 📄 Resume Screening")

    file = st.file_uploader("Upload Resume (.txt)", type=["txt"])

    skills = ["python", "sql", "machine learning"]

    if file:
        text = file.read().decode("utf-8").lower()
        found = [s for s in skills if s in text]

        st.markdown("### ✅ Skills Found")
        st.write(found)

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
<li>Screen resumes automatically</li>
</ul>
</p>
</div>
""", unsafe_allow_html=True)
