import streamlit as st

st.set_page_config(page_title="HR AI System", layout="wide")

# ===== SIDEBAR STYLE =====
st.markdown("""
<style>
/* Expand sidebar width */
section[data-testid="stSidebar"] {
    width: 260px !important;
}

/* Sidebar title */
[data-testid="stSidebarNav"]::before {
    content: "💼 HR AI System";
    font-size: 22px;
    font-weight: bold;
    margin-left: 15px;
    margin-top: 20px;
    margin-bottom: 20px;
    display: block;
}

/* Improve spacing */
[data-testid="stSidebarNav"] ul {
    padding-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ===== MAIN PAGE =====
st.title("👋 Welcome to HR AI System")

st.write("""
### Navigate using the sidebar →

- 📊 HR Dashboard  
- 🤖 Predict Attrition  
- 📄 Resume Screening  
- 📘 About  

---

🚀 This system helps HR teams make smarter decisions using AI.
""")
