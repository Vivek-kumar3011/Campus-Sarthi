import streamlit as st
import pandas as pd

# Gymkhana contacts data
contacts = [
    {"Position": "Vice President", "Name": "Varun Jaiswal"},
    {"Position": "Treasurer", "Name": "Thejus K"},
    {"Position": "General Secretary (Sports)", "Name": "Aman Kumar"},
    {"Position": "General Secretary (Culture)", "Name": "Yashwanth Sai Rayidi"},
    {"Position": "General Secretary (Tech)", "Name": "Nitin Pratap"},
    {"Position": "General Secretary (Student Affairs)", "Name": "Anmol Mishra"},
    {"Position": "Secretary (Indoor Sports)", "Name": "Ankit Kumar Soni"},
    {"Position": "Secretary (Outdoor Sports)", "Name": "Souradeep Bagchi"},
    {"Position": "Secretary (Symphony)", "Name": "S Harikesh"},
    {"Position": "Secretary (Spotlight)", "Name": "Satyam Babu"},
    {"Position": "Secretary (GroovZ)", "Name": "Anushka Jhinghram"},
    {"Position": "Secretary (Pixel)", "Name": "Aditya Arya"},
    {"Position": "Secretary (Robotics Club)", "Name": "Chirag Shukla"},
    {"Position": "Secretary (Student Affairs and Welfare)", "Name": "Dhanavath Samith Raj"},
    {"Position": "Secretary (CodeCubes)", "Name": "Subhadeep Mandal"},
    {"Position": "Secretary (Freescape)", "Name": "Bhaskar Metiya"},
    {"Position": "Secretary (Udaan)", "Name": "Joshua Ayush Kerketta"},
]

# Generate email addresses (firstname.lastname@gmail.com)
for c in contacts:
    name_parts = c["Name"].split()
    email = ".".join([part.lower() for part in name_parts]) + "@gmail.com"
    # clickable mailto link
    c["Email"] = f"[{email}](mailto:{email})"

def show():
    st.title("🏛 Gymkhana Contacts")

    # Convert to DataFrame
    df = pd.DataFrame(contacts)

    # Reset index to start from 1
    df.index = df.index + 1

    # Show table with clickable links
    st.markdown(df.to_markdown(), unsafe_allow_html=True)
