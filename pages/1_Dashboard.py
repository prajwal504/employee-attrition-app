import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 HR Dashboard")

# Dummy data
data = pd.DataFrame({
    "Department": ["HR", "IT", "Sales", "Finance"],
    "Employees": [10, 25, 15, 8]
})

st.bar_chart(data.set_index("Department"))

# Attrition sample chart
attrition = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Attrition": [2, 3, 1, 4]
})

st.line_chart(attrition.set_index("Month"))
