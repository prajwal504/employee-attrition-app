import streamlit as st
import pandas as pd

st.title("📊 HR Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Employees", "58")
col2.metric("Attrition Rate", "12%")
col3.metric("Avg Satisfaction", "3.8/5")

st.write("---")

# Charts
data = pd.DataFrame({
    "Department": ["HR", "IT", "Sales", "Finance"],
    "Employees": [10, 25, 15, 8]
})

st.subheader("👥 Employees by Department")
st.bar_chart(data.set_index("Department"))

attrition = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Attrition": [2, 3, 1, 4]
})

st.subheader("📉 Monthly Attrition")
st.line_chart(attrition.set_index("Month"))
