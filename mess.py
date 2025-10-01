import streamlit as st
from datetime import datetime

# Weekly mess menu
from mess_data import MESS_MENU   # keep dictionary in mess_data.py for cleaner code

def show():
    st.header("🍴 Campus Mess Menu")

    today = datetime.now().strftime("%A")  # Get current day name
    st.subheader(f"Today's Menu ({today})")

    if today in MESS_MENU:
        menu = MESS_MENU[today]
        for meal, items in menu.items():
            st.markdown(f"### {meal}")
            st.write(items)
    else:
        st.info("No menu available for today.")

    # Allow students to check other days too
    st.subheader("📅 View Other Days")
    day = st.selectbox("Select Day", list(MESS_MENU.keys()))
    menu = MESS_MENU[day]
    for meal, items in menu.items():
        st.markdown(f"### {meal}")
        st.write(items)
