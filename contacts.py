import streamlit as st
import pandas as pd

# ---------------- Faculty Contacts ----------------
faculty = [
    {"Name": "Prof. Santanu Chattopadhyay", "Email": "director@iiitkalyani.ac.in"},
    {"Name": "Dr. Amit Ranjan Azad", "Email": "amitranjanazad@iiitkalyani.ac.in"},
    {"Name": "Dr. Anirban Lakshman", "Email": "anirban@iiitkalyani.ac.in"},
    {"Name": "Dr. Bhaskar Biswas", "Email": "bhaskar@iiitkalyani.ac.in"},
    {"Name": "Dr. Dalia Nandi (Das)", "Email": "dalia@iiitkalyani.ac.in"},
    {"Name": "Dr. Debasish Bera", "Email": "debasish@iiitkalyani.ac.in"},
    {"Name": "Dr. Imon Mukherjee", "Email": "imon@iiitkalyani.ac.in"},
    {"Name": "Dr. Oishila Bandyopadhyay", "Email": "oishila@iiitkalyani.ac.in"},
    {"Name": "Dr. Pratik Chakraborty", "Email": "pratik@iiitkalyani.ac.in"},
    {"Name": "Prof. (Dr.) Rabindranath Bera (Visiting Professor)", "Email": "rbera@iiitkalyani.ac.in"},
    {"Name": "Dr. Rinky Sha", "Email": "rinky@iiitkalyani.ac.in"},
    {"Name": "Dr. Sanjay Chatterji", "Email": "sanjayc@iiitkalyani.ac.in"},
    {"Name": "Dr. Sanjoy Pratihar", "Email": "sanjoy@iiitkalyani.ac.in"},
    {"Name": "Dr. SK Hafizul Islam", "Email": "hafi786@iiitkalyani.ac.in"},
    {"Name": "Dr. Soumen Pandit", "Email": "soumen@iiitkalyani.ac.in"},
    {"Name": "Dr. Sudeshna Mondal", "Email": "sudeshna@iiitkalyani.ac.in"},
    {"Name": "Dr. Uma Das", "Email": "uma@iiitkalyani.ac.in"},
]

# ---------------- Office Contacts ----------------
office = [
    {"Office": "Director", "Email": "director@iiitkalyani.ac.in"},
    {"Office": "Registrar", "Email": "registrar@iiitkalyani.ac.in"},
    {"Office": "Assistant Registrar (Academics)", "Email": "ar.academic@iiitkalyani.ac.in"},
    {"Office": "Assistant Registrar (Administration)", "Email": "ar.admin@iiitkalyani.ac.in"},
    {"Office": "Finance Office", "Email": "finance@iiitkalyani.ac.in"},
]

def make_clickable(df, email_col):
    df[email_col] = df[email_col].apply(
        lambda x: f"[{x}](mailto:{x})" if pd.notna(x) and x.strip() != "" else ""
    )
    df.index = df.index + 1
    return df

def show():
    st.title("📞 IIIT Kalyani Contacts")

    # ---------- Faculty Table ----------
    st.subheader("👨‍🏫 Faculty Contacts")
    faculty_df = pd.DataFrame(faculty)
    faculty_df = make_clickable(faculty_df, "Email")
    st.markdown(faculty_df.to_markdown(index=True), unsafe_allow_html=True)

    # ---------- Office Table ----------
    st.subheader("🏢 Office Contacts")
    office_df = pd.DataFrame(office)
    office_df = make_clickable(office_df, "Email")
    st.markdown(office_df.to_markdown(index=True), unsafe_allow_html=True)
