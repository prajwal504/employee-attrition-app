import streamlit as st
import re

st.title("📄 Resume Screening")

uploaded_file = st.file_uploader("Upload Resume (txt)", type=["txt"])

skills = ["python", "machine learning", "sql", "data analysis"]

if uploaded_file:
    text = uploaded_file.read().decode("utf-8").lower()

    found_skills = [skill for skill in skills if skill in text]

    st.write("### ✅ Extracted Skills:")
    st.write(found_skills)

    st.write(f"### 📊 Score: {len(found_skills)}")
