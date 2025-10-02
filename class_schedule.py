# app.py
import streamlit as st
import pandas as pd
from datetime import datetime
from class_data import CLASS_SCHEDULE_DATA, ALL_DAYS, FACULTY_LIST

def show():
    """Renders the Streamlit dashboard for class schedule management."""
    st.title("🏛️ IIITK Autumn Semester Schedule Dashboard")
    st.markdown("Select a **Branch/Semester** and **Day** to view your class schedule.")

    # --- Layout for Filters ---
    col1, col2 = st.columns([2, 1])

    # Branch/Semester Selection
    branch_options = list(CLASS_SCHEDULE_DATA.keys())
    selected_branch = col1.selectbox("Select Branch/Semester", ["-- Select --"] + branch_options)

    # --- Default day = Today ---
    full_to_short = {
        "MONDAY": "MON",
        "TUESDAY": "TUE",
        "WEDNESDAY": "WED",
        "THURSDAY": "THU",
        "FRIDAY": "FRI",
        "SATURDAY": "SAT",
        "SUNDAY": "SUN"
    }

    today_full = datetime.now().strftime("%A").upper()  # e.g. "THURSDAY"
    today_name = full_to_short.get(today_full, "MON")   # Map to "THU"

    try:
        default_index = ALL_DAYS.index(today_name)
    except ValueError:
        default_index = 0

    selected_day = col2.selectbox("Select Day", ALL_DAYS, index=default_index)

    st.markdown("---")

    # --- Show Schedule only if branch is selected ---
    if selected_branch != "-- Select --":
        st.header(f"Schedule for **{selected_branch}** on **{selected_day}**")

        branch_schedule = CLASS_SCHEDULE_DATA.get(selected_branch, {})
        display_schedule = branch_schedule.get(selected_day, [])

        if display_schedule:
            df = pd.DataFrame(display_schedule)

            # Rename columns
            df.columns = ["Time Slot", "Course Code", "Room", "Faculty Code"]

            # Map Faculty Code → Faculty Name
            df['Faculty Name'] = df['Faculty Code'].apply(
                lambda x: FACULTY_LIST.get(x.split(',')[0].strip(), x)
            )

            st.dataframe(
                df[["Time Slot", "Course Code", "Room", "Faculty Name", "Faculty Code"]],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info(f"No classes scheduled on **{selected_day}** for **{selected_branch}** 🎉. Please check another day or semester.")

    else:
        st.warning("👆 Please select a **Branch/Semester** to view the schedule.")

    st.markdown("---")

    # --- Permanent Faculty Code Reference Table ---
    st.subheader("📌 Faculty Code Reference")
    faculty_df = pd.DataFrame(FACULTY_LIST.items(), columns=["Code", "Faculty Name"])
    st.dataframe(faculty_df, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title="IIITK Class Schedule App",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    show()
