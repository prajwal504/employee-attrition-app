st.title("📄 Resume Screening")

file = st.file_uploader("Upload Resume", type=["txt"])

skills = ["python", "sql", "machine learning", "data analysis"]

if file:
    text = file.read().decode("utf-8").lower()

    found = [s for s in skills if s in text]

    st.subheader("✅ Skills Found")
    st.write(found)

    score = len(found)

    st.progress(score * 25)

    if score >= 3:
        st.success("Strong Candidate")
    else:
        st.warning("Needs Improvement")
