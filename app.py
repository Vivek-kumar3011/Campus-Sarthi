import streamlit as st

# Import feature modules
import mess
import class_schedule
import lost_found
import buy_sell
import notices
import academic_resources
import college_contacts
import opportunities
import chatbot
import task

st.sidebar.title("🏫 Campus Sarthi")
section = st.sidebar.radio(
    "Navigate",
    [
        "Mess Menu", "Class Schedule", "Notices / Events", "Academic Resources",
        "Opportunities", "College Contacts", "Task Manager",
        "Lost & Found", "Buy & Sell", "Chatbot" 
    ]
)

if section == "Class Schedule":
    class_schedule.show()

elif section == "Mess Menu":
    mess.show()

elif section == "Notices / Events":
    notices.show()

elif section == "Academic Resources":
    academic_resources.show()

elif section == "Opportunities":
    opportunities.show()

elif section == "College Contacts":
    college_contacts.show()

elif section == "Task Manager":
    task.show()

elif section == "Chatbot":
    chatbot.show()

elif section == "Lost & Found":
    lost_found.show()

elif section == "Buy & Sell":
    buy_sell.show()