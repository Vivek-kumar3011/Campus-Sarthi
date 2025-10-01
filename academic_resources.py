import streamlit as st

def show():
    st.header("📚 Academic Resources")

    st.subheader("1️⃣ Previous Year Question Papers (PYQs)")
    st.markdown(
        "[Access PYQs Here](https://drive.google.com/drive/u/0/folders/1X3AEV93QzFJU531xGhjzTGuRuUYpjXcd)",
        unsafe_allow_html=True
    )

    st.subheader("2️⃣ GPA Calculator")
    st.markdown(
        "[Use GPA Calculator Here](https://gpa-calculator-gold.vercel.app/)",
        unsafe_allow_html=True
    )

    # You can add more resources here
    # st.subheader("3️⃣ Additional Resources (Optional)")
    # st.markdown("- Study materials, notes, reference links, etc.")
