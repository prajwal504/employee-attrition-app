import streamlit as st

st.set_page_config(page_title="HR AI System", layout="wide")

# Simple login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🔐 HR AI System Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.session_state.logged_in = True
        st.success("Login Successful!")
    else:
        st.error("Invalid credentials")

if st.session_state.logged_in:
    st.info("Go to the sidebar to access features 🚀")
