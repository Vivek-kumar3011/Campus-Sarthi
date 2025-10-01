import streamlit as st
from datetime import datetime

# Import data from the mess_data.py file
from mess_data import MESS_MENU, TIME_SLOTS, MESS_NOTES

def show():
    st.header("🍴 Campus Mess Menu")
    
    # --- Today's Menu Section ---
    today = datetime.now().strftime("%A") 
    st.subheader(f"Today's Menu ({today})")

    if today in MESS_MENU:
        menu = MESS_MENU[today]
        for meal, items in menu.items():
            time_slot = TIME_SLOTS.get(meal, "") 
            # Display meal name and its corresponding time slot
            st.markdown(f"### {meal} {time_slot}") 
            st.write(items)
    else:
        st.info("No menu available for today.")
        
    st.markdown("---")
    
    # --- Notes Section ---
    st.subheader("📝 Important Notes")
    # Display notes, replacing newline characters with HTML line breaks for better rendering
    st.markdown(MESS_NOTES.replace('\n', '<br>'), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # --- View Other Days Section ---
    st.subheader("📅 View Other Days")
    
    # Ensure the current day is the default selection
    default_index = list(MESS_MENU.keys()).index(today) if today in MESS_MENU else 0
    day = st.selectbox("Select Day", list(MESS_MENU.keys()), index=default_index)
    
    menu = MESS_MENU[day]
    for meal, items in menu.items():
        time_slot = TIME_SLOTS.get(meal, "")
        # Display meal name and its corresponding time slot
        st.markdown(f"### {meal} {time_slot}")
        st.write(items)

# Run the application
if __name__ == "__main__":
    show()