# app.py
import streamlit as st
import pandas as pd
from datetime import datetime
# Import data from the other file
from class_data import CLASS_SCHEDULE_DATA, ALL_DAYS, FACULTY_LIST

def show():
    """Renders the Streamlit dashboard for class schedule management."""
    st.title("🏛️ IIITK Autumn Semester Schedule Dashboard")
    st.markdown("Use the **sidebar filters** to view class schedules by **Branch/Semester** and **Day**.")

    # --- Sidebar Filters ---
    st.sidebar.header("Filter Options")
    
    # 1. Branch/Semester Selection (Now only contains the 8 requested options)
    branch_options = list(CLASS_SCHEDULE_DATA.keys())
    selected_branch = st.sidebar.selectbox(
        "Select Branch/Semester", 
        branch_options
    )
    
    # Get the schedule for the selected branch, defaulting to empty if not found
    branch_schedule = CLASS_SCHEDULE_DATA.get(selected_branch, {})

    # 2. Day Selection
    # FIX: Use the global ALL_DAYS list for the selectbox options and for correct indexing.
    # This guarantees the order is always correct (MON, TUE, WED...) and predictable.
    available_days = ALL_DAYS 

    # Logic to set the default day to the current day
    today_name = datetime.now().strftime("%A").upper() # Gets 'WEDNESDAY'
    
    # Find the index of the current day in the full ALL_DAYS list (guaranteed to be there).
    try:
        default_index = available_days.index(today_name)
    except ValueError:
        # Default to Monday if today is Sunday or an unexpected value
        default_index = 0
    
    selected_day = st.sidebar.selectbox(
        "View Schedule for Day:", 
        available_days, # Use the fixed ALL_DAYS list
        index=default_index # <-- This will now correctly set 'WED'
    )
    
    # For display consistency: if the selected day is not an active key in the schedule (e.g., Saturday class for a MON-FRI only schedule), 
    # we still display the day, but show the 'No classes' message below.

    st.markdown("---")

    # --- Display Filtered Schedule ---
    st.header(f"Schedule for **{selected_branch}** on **{selected_day}**")
    
    # Get the day's schedule. This will be an empty list [] if no classes are scheduled.
    display_schedule = branch_schedule.get(selected_day, [])
    
    if display_schedule:
        # Convert the list of dicts to a pandas DataFrame for a clean table view
        df = pd.DataFrame(display_schedule)
        
        # Rename and format columns
        df.columns = ["Time Slot", "Course Code", "Room", "Faculty Code"]
        
        # Add full faculty name for clarity by mapping the code
        df['Faculty Name'] = df['Faculty Code'].apply(lambda x: FACULTY_LIST.get(x.split(',')[0].strip(), x))
        
        st.dataframe(
            df[["Time Slot", "Course Code", "Room", "Faculty Name", "Faculty Code"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info(f"No classes scheduled on **{selected_day}** for **{selected_branch}** 🎉. Please check another day or semester.")
        
    st.markdown("---")

    # --- Reference Table ---
    with st.expander("View Full Faculty Code List"):
        st.subheader("Faculty Code Reference")
        faculty_df = pd.DataFrame(FACULTY_LIST.items(), columns=["Code", "Faculty Name"])
        st.dataframe(faculty_df, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title="IIITK Class Schedule App",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    # Start the dashboard function
    show()