import streamlit as st
import pandas as pd

def make_clickable(email):
    return f'<a href="mailto:{email}">{email}</a>'

def show():
    st.title("📞 College Contacts")

    # -------------------- Office Contacts --------------------
    st.subheader("🏢 Office Contacts")

    office_data = [
        {"Name": "Prof. Santanu Chattopadhyay (Director)", "Email": "director@iiitkalyani.ac.in"},
        {"Name": "Registrar", "Email": "registrar@iiitkalyani.ac.in"},
        {"Name": "Asst. Registrar", "Email": "asstregistrar@iiitkalyani.ac.in"},
        {"Name": "Finance Officer", "Email": "finance@iiitkalyani.ac.in"}
    ]
    office_df = pd.DataFrame(office_data)
    office_df["Email"] = office_df["Email"].apply(make_clickable)
    office_df.index = office_df.index + 1
    st.markdown(office_df.to_html(escape=False, index=True), unsafe_allow_html=True)

    # -------------------- Gymkhana Contacts --------------------
    st.subheader("🎯 Gymkhana Contacts")

    gymkhana_data = [
        {"Name": "DHANAVATH SAMITH RAJ", "Club Secretary": "Vice President", "Email": "cse22042@iiitkalyani.ac.in"},
        {"Name": "ANMOL MISHRA", "Club Secretary": "Treasurer", "Email": "ece22121@iiitkalyani.ac.in"},
        {"Name": "NIKHIL TIWARI", "Club Secretary": "General Secretary - Sports", "Email": "ece23126@iiitkalyani.ac.in"},
        {"Name": "AYUSH PRASAD", "Club Secretary": "General Secretary - Tech", "Email": "cse23031@iiitkalyani.ac.in"},
        {"Name": "KALYANI HEMANTH", "Club Secretary": "General Secretary - Culture", "Email": "cse23056@iiitkalyani.ac.in"},
        {"Name": "DIGVIJAY TOMAR", "Club Secretary": "General Secretary - Student Affairs", "Email": "cse23043@iiitkalyani.ac.in"},
        {"Name": "RISHABH KARTIK", "Club Secretary": "Secretary - Pixel", "Email": "cse23077@iiitkalyani.ac.in"},
        {"Name": "ANSHU KUMAR", "Club Secretary": "Secretary - Robotics", "Email": "cse23109@iiitkalyani.ac.in"},
        {"Name": "AMAN KUMAR", "Club Secretary": "Secretary - Codecubus", "Email": "cse23012@iiitkalyani.ac.in"},
        {"Name": "MD ZAID FAISHAL", "Club Secretary": "Secretary - Freescape", "Email": "cse23067@iiitkalyani.ac.in"},
        {"Name": "AAHANA PRIYA", "Club Secretary": "Secretary - Symphony", "Email": "ece23108@iiitkalyani.ac.in"},
        {"Name": "ESHA BISWAS", "Club Secretary": "Secretary - Groovz", "Email": "cse23125@iiitkalyani.ac.in"},
        {"Name": "KRITYA RAJANSH", "Club Secretary": "Secretary - Udaan", "Email": "cse23063@iiitkalyani.ac.in"},
        {"Name": "PADALA SAI SHANKAR", "Club Secretary": "Secretary - Spotlight", "Email": "ece23128@iiitkalyani.ac.in"},
        {"Name": "DARURI AKASH", "Club Secretary": "Secretary - Outdoor Sports", "Email": "cse23036@iiitkalyani.ac.in"},
        {"Name": "NENAVATH RANAPRATHAP RATHOD", "Club Secretary": "Secretary - Indoor Sports", "Email": "cse23069@iiitkalyani.ac.in"},
        {"Name": "RATHOD SAIGANESH", "Club Secretary": "Secretary - Students Affairs", "Email": "cse23076@iiitkalyani.ac.in"},
    ]
    gymkhana_df = pd.DataFrame(gymkhana_data)
    gymkhana_df["Email"] = gymkhana_df["Email"].apply(make_clickable)
    gymkhana_df.index = gymkhana_df.index + 1
    st.markdown(gymkhana_df.to_html(escape=False, index=True), unsafe_allow_html=True)

    # -------------------- Teacher Contacts --------------------
    st.subheader("👨‍🏫 Teacher Contacts")

    teacher_data = [
        {"Name": "Dr. Amit Ranjan Azad", "Email": "amitranjanazad@iiitkalyani.ac.in"},
        {"Name": "Dr. Anirban Lakshman", "Email": "anirban@iiitkalyani.ac.in"},
        {"Name": "Dr. Bhaskar Biswas", "Email": "bhaskar@iiitkalyani.ac.in"},
        {"Name": "Dr. Dalia Nandi (Das)", "Email": "dalia@iiitkalyani.ac.in"},
        {"Name": "Dr. Debasish Bera", "Email": "debasish@iiitkalyani.ac.in"},
        {"Name": "Dr. Imon Mukherjee", "Email": "imon@iiitkalyani.ac.in"},
        {"Name": "Dr. Oishila Bandyopadhyay", "Email": "oishila@iiitkalyani.ac.in"},
        {"Name": "Dr. Pratik Chakraborty", "Email": "pratik@iiitkalyani.ac.in"},
        {"Name": "Prof. (Dr.) Rabindranath Bera", "Email": "rbera@iiitkalyani.ac.in"},
        {"Name": "Dr. Rinky Sha", "Email": "rinky@iiitkalyani.ac.in"},
        {"Name": "Dr. Sanjay Chatterji", "Email": "sanjayc@iiitkalyani.ac.in"},
        {"Name": "Dr. Sanjoy Pratihar", "Email": "sanjoy@iiitkalyani.ac.in"},
        {"Name": "Dr. SK Hafizul Islam", "Email": "hafi786@iiitkalyani.ac.in"},
        {"Name": "Dr. Soumen Pandit", "Email": "soumen@iiitkalyani.ac.in"},
        {"Name": "Dr. Sudeshna Mondal", "Email": "sudeshna@iiitkalyani.ac.in"},
        {"Name": "Dr. Uma Das", "Email": "uma@iiitkalyani.ac.in"},
    ]
    teacher_df = pd.DataFrame(teacher_data)
    teacher_df["Email"] = teacher_df["Email"].apply(make_clickable)
    teacher_df.index = teacher_df.index + 1
    st.markdown(teacher_df.to_html(escape=False, index=True), unsafe_allow_html=True)

    # -------------------- Anti Ragging --------------------
    st.subheader("🚨 Anti-Ragging Helpline")
    st.markdown("""
    📧 Email: <a href="mailto:antiragging@iiitkalyani.ac.in">antiragging@iiitkalyani.ac.in</a><br>
    📞 Contact: +91-1800-180-5522
    """, unsafe_allow_html=True)