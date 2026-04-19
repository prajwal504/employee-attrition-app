if st.button("Predict"):

    overtime_val = 1 if overtime == "Yes" else 0

    input_data = pd.DataFrame([[age, salary, years, overtime_val, satisfaction]],
                              columns=['age','salary','years_at_company','overtime','job_satisfaction'])

    pred = model.predict(input_data)
    prob = model.predict_proba(input_data)

    confidence = prob[0][pred[0]] * 100

    if pred[0] == 1:
        st.error(f"⚠️ High Risk ({confidence:.2f}%)")
        st.write("💡 Improve satisfaction & reduce overtime")

    else:
        st.success(f"✅ Low Risk ({confidence:.2f}%)")
        st.write("👍 Employee is stable")
