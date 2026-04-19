import streamlit as st

# ===== CONFIG =====
st.set_page_config(page_title="HR AI System", layout="wide")

# ===== LIGHT CLEAN UI =====
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #2c3e50;
}
.subtitle {
    text-align: center;
    color: #555;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="title">💼 HR AI System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered employee attrition analysis</div>', unsafe_allow_html=True)

st.write("---")

# ===== NAVIGATION (WORKING) =====
page = st.radio(
    "Navigate",
    ["📊 Dashboard", "🤖 Predict", "📄 Resume Screening", "📘 About"],
    horizontal=True
)

# ===== ROUTING (NO ERRORS) =====
if page == "📊 Dashboard":
    st.switch_page("pages/1_HR_Dashboard.py")

elif page == "🤖 Predict":
    st.switch_page("pages/2_Predict.py")

elif page == "📄 Resume Screening":
    st.switch_page("pages/3_Resume_Screening.py")

elif page == "📘 About":
    st.switch_page("pages/4_About.py")
