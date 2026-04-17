import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="HR AI Dashboard", layout="wide")

# Load model
model = joblib.load("attrition_model.pkl")

# ===== PREMIUM CSS =====
st.markdown("""
<style>
body {
    background-color: #0E1117;
}
.main {
    background-color: #0E1117;
}

/* Title */
h1 {
    color: #00FFAA;
    text-align: center;
    font-size: 40px;
}

/* Card style */
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,255,170,0.2);
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #00FFAA, #00cc88);
    color: black;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}

/* Text */
.stMarkdown {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
st.sidebar.title("🚀 HR AI Dashboard")
page = st.sidebar.radio("Navigation", ["🏠 Home", "📘 About"])

# ===== ABOUT PAGE =====
if page == "📘 About":
    st.title("📘 About This Project")
    st.markdown("""
    ### 💼 Smart HR AI System
    
    This system predicts employee attrition using Machine Learning.
    
    #### 🔍 Features:
    - AI-based Attrition Prediction  
    - Real-time analysis  
    - Clean UI dashboard  
    
    #### 🤖 Model:
    - Random Forest Classifier
    
    #### 📊 Inputs:
    Age, Salary, Experience, Overtime, Satisfaction
    """)

# ===== HOME PAGE =====
else:
    st.title("💼 Smart HR AI System")

    st.markdown("### 🔮 Predict Employee Attrition Instantly")

    # Layout
    col1, col2 = st.columns([1, 1])

    # ===== INPUT CARD =====
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📊 Employee Details")

        age = st.number_input("Age", 18, 60)
        salary = st.number_input("Salary", 10000, 200000)
        years = st.number_input("Years at Company", 0, 40)
        overtime = st.selectbox("Overtime", [0, 1])
        satisfaction = st.slider("Job Satisfaction", 1, 5)

        st.markdown('</div>', unsafe_allow_html=True)

    # ===== OUTPUT CARD =====
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🤖 Prediction Result")

        if st.button("🚀 Predict Now"):
            input_data = pd.DataFrame([[age, salary, years, overtime, satisfaction]],
                                      columns=['age', 'salary', 'years_at_company', 'overtime', 'job_satisfaction'])

            prediction = model.predict(input_data)
            prob = model.predict_proba(input_data)

            risk = prediction[0]
            confidence = prob[0][risk] * 100

            # Progress bar
            st.progress(int(confidence))

            if risk == 1:
                st.error(f"⚠️ High Risk of Attrition ({confidence:.2f}%)")
                st.markdown("""
                ### 💡 Suggestions:
                - Improve job satisfaction  
                - Reduce overtime  
                - Increase engagement  
                """)
            else:
                st.success(f"✅ Low Risk of Attrition ({confidence:.2f}%)")
                st.markdown("""
                ### 👍 Status:
                - Employee is stable  
                - Maintain current environment  
                """)

        st.markdown('</div>', unsafe_allow_html=True)
