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

st.sidebar.title("🏫 Campus Sarthi")
section = st.sidebar.radio(
    "Navigate",
    [
        "Mess Menu", "Class Schedule", "Lost & Found", "Buy & Sell",
        "Notices / Events", "Academic Resources", "College Contacts"
        , "Opportunities & Updates", "Chatbot"
    ]
)

if section == "Mess Menu":
    mess.show()

elif section == "Class Schedule":
    class_schedule.show()

elif section == "Lost & Found":
    lost_found.show()

elif section == "Buy & Sell":
    buy_sell.show()

elif section == "Notices / Events":
    notices.show()

elif section == "Academic Resources":
    academic_resources.show()

elif section == "College Contacts":
    college_contacts.show()

elif section == "Opportunities & Updates":
    opportunities.show()

elif section == "Chatbot":
    chatbot.show()
