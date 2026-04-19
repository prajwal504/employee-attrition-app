import streamlit as st
import pandas as pd
import joblib

# CONFIG
st.set_page_config(page_title="HR AI System", layout="wide")

model = joblib.load("attrition_model.pkl")

# ===== CSS (STARTUP STYLE) =====
st.markdown("""
<style>

/* Page background */
body {
    background-color: #f9fafc;
}

/* Hero section */
.hero {
    text-align: center;
    padding: 60px 20px;
}

.hero h1 {
    font-size: 48px;
    color: #2c3e50;
}

.hero p {
    font-size: 20px;
    color: #555;
}

/* Feature cards */
.card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
}

/* Buttons */
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

/* Result box */
.result {
    padding: 20px;
    border-radius: 10px;
    font-size: 18px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# ===== HERO SECTION =====
st.markdown("""
<div class="hero">
<h1>💼 HR AI System</h1>
<p>Predict Employee Attrition using AI and make smarter HR decisions</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ===== FEATURES SECTION =====
st.markdown("### 🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">🤖<br><b>AI Prediction</b><br>Predict employee attrition instantly</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">⚡<br><b>Real-time Analysis</b><br>Get results instantly</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">📊<br><b>Smart Insights</b><br>Understand employee behavior</div>', unsafe_allow_html=True)

st.write("---")

# ===== HOW IT WORKS =====
st.markdown("### ⚙️ How It Works")

st.write("""
1. Enter employee details  
2. AI model analyzes patterns  
3. Get prediction with confidence  
""")

st.write("---")

# ===== MAIN TOOL =====
st.markdown("### 🔮 Try the Model")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Input Details")

    age = st.number_input("Age", 18, 60)
    salary = st.number_input("Salary", 10000, 200000)
    years = st.number_input("Years at Company", 0, 40)
    overtime = st.selectbox("Overtime", ["No", "Yes"])
    satisfaction = st.slider("Job Satisfaction", 1, 5)

with col2:
    st.subheader("📊 Result")

    if st.button("Predict Now 🚀"):

        overtime_val = 1 if overtime == "Yes" else 0

        input_data = pd.DataFrame([[age, salary, years, overtime_val, satisfaction]],
                                  columns=['age','salary','years_at_company','overtime','job_satisfaction'])

        pred = model.predict(input_data)
        prob = model.predict_proba(input_data)

        confidence = prob[0][pred[0]] * 100

        if pred[0] == 1:
            st.markdown(f"""
            <div class="result" style="background:#ffe6e6; color:#c0392b;">
            ⚠️ High Risk of Attrition<br>
            Confidence: {confidence:.2f}%
            </div>
            """, unsafe_allow_html=True)

            st.write("### 💡 Suggestions")
            st.write("- Improve satisfaction")
            st.write("- Reduce overtime")
            st.write("- Offer incentives")

        else:
            st.markdown(f"""
            <div class="result" style="background:#eafaf1; color:#27ae60;">
            ✅ Low Risk of Attrition<br>
            Confidence: {confidence:.2f}%
            </div>
            """, unsafe_allow_html=True)

            st.write("### 👍 Status")
            st.write("- Employee stable")
            st.write("- Maintain environment")

st.write("---")

# ===== FOOTER =====
st.markdown("""
<center>
© 2026 HR AI System | Built for smarter workforce decisions
</center>
""", unsafe_allow_html=True)
