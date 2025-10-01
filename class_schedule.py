import streamlit as st
from datetime import datetime
from class_data import CLASS_SCHEDULE

def show():
    st.header("📚 Class Schedule")

    # Semester selection
    semester = st.radio("Select Semester", ["1st Semester", "3rd Semester"])

    today = datetime.now().strftime("%A")
    st.subheader(f"Today's Schedule ({today}) - {semester}")

    if today in CLASS_SCHEDULE[semester]:
        schedule = CLASS_SCHEDULE[semester][today]
        for item in schedule:
            st.markdown(f"**{item['time']}** — {item['course']} ({item['faculty']}) in {item['room']}")
    else:
        st.info("No classes today 🎉")

    # Allow user to check other days
    st.subheader("📅 View Other Days")
    day = st.selectbox("Select Day", list(CLASS_SCHEDULE[semester].keys()))
    schedule = CLASS_SCHEDULE[semester][day]
    for item in schedule:
        st.markdown(f"**{item['time']}** — {item['course']} ({item['faculty']}) in {item['room']}")
