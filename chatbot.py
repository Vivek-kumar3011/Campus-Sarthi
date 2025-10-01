# app.py
import streamlit as st
import pandas as pd
from datetime import datetime
from class_data import CLASS_SCHEDULE_DATA, ALL_DAYS, FACULTY_LIST

# --- Helper Functions ---

def draw_sidebar_navigation():
    """Draws the main navigation radio buttons once and returns the selection."""
    
    # 1. Draw the application title once
    st.sidebar.header("🏫 Campus Sarthi")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Campus Features")
    
    # The list of menu items
    menu_items = [
        "Mess Menu", "Class Schedule", "Lost & Found", "Buy & Sell", 
        "Notices / Events", "Academic Resources", "College Contacts", 
        "Opportunities & Updates", 
        "Chatbot"
    ]
    
    # Set default selection to "Class Schedule"
    selected_feature = st.sidebar.radio("Navigate:", menu_items, index=menu_items.index("Class Schedule"))
    
    return selected_feature

def show_schedule(filter_container):
    """Renders the Class Schedule content and conditionally populates the filter_container."""
    
    st.title("🏛️ Campus-Sarthi: Class Schedule")
    st.markdown("Use the **sidebar filters** to view class schedules by **Branch/Semester** and **Day**.")

    # --- CONDITIONAL SIDEBAR FILTERS ---
    # The filter container is st.sidebar itself, passed from show()
    with filter_container: 
        st.header("Filter Options")
        
        branch_options = list(CLASS_SCHEDULE_DATA.keys())
        selected_branch = st.selectbox(
            "Select Branch/Semester", 
            branch_options
        )
        
        available_days = ALL_DAYS 
        today_name = datetime.now().strftime("%A").upper() 
        
        try:
            default_index = available_days.index(today_name)
        except ValueError:
            default_index = 0
            
        selected_day = st.selectbox(
            "View Schedule for Day:", 
            available_days, 
            index=default_index,
            key='schedule_day_selector' 
        )
        
        st.markdown("---")
    
    # --- CONTENT DISPLAY (Rest of the show_schedule function) ---
    branch_schedule = CLASS_SCHEDULE_DATA.get(selected_branch, {})

    st.header(f"Schedule for **{selected_branch}** on **{selected_day}**")
    
    display_schedule = branch_schedule.get(selected_day, [])
    
    if display_schedule:
        df = pd.DataFrame(display_schedule)
        df.columns = ["Time Slot", "Course Code", "Room", "Faculty Code"]
        df['Faculty Name'] = df['Faculty Code'].apply(lambda x: FACULTY_LIST.get(x.split(',')[0].strip(), x))
        
        st.dataframe(
            df[["Time Slot", "Course Code", "Room", "Faculty Name", "Faculty Code"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info(f"No classes scheduled on **{selected_day}** for **{selected_branch}** 🎉. Please check another day or semester.")
        
    st.markdown("---")

    with st.expander("View Full Faculty Code List"):
        st.subheader("Faculty Code Reference")
        faculty_df = pd.DataFrame(FACULTY_LIST.items(), columns=["Code", "Faculty Name"])
        st.dataframe(faculty_df, use_container_width=True, hide_index=True)


def show_chatbot_feature(filter_container):
    """Renders the Chatbot feature interface."""
    
    # 1. Clear the placeholder container for filters
    filter_container.empty()
    
    st.header("🤖 Campus Chatbot")
    st.write("Ask me about mess, classes, contacts, or anything campus related!")

    # 2. Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # 3. Chat Input and Logic (using a form for clean submission and state update)
    with st.form(key='chatbot_form', clear_on_submit=True):
        query = st.text_input("You:", key='user_input')
        submit_button = st.form_submit_button(label='Send')
    
    # 4. Process Query and Update History
    if submit_button and query:
        response = "Sorry, I don't understand that. Try asking about a feature like 'Mess Menu' or 'Anti-Ragging'."
        q_lower = query.lower()

        # --- Keyword-Based Responses ---
        if "mess" in q_lower or "menu" in q_lower:
            response = "You can check the mess menu in the **Mess Menu** section."
        elif "class" in q_lower or "schedule" in q_lower:
            response = "Go to **Class Schedule** section to see today's classes."
        elif "lost" in q_lower or "found" in q_lower:
            response = "Lost something? Post it in **Lost & Found** section."
        elif "sell" in q_lower or "buy" in q_lower or "cycle" in q_lower:
             response = """
            🚲 **Selling or Buying Items:**
            The best way is to use the **Buy & Sell** feature. Create a listing there with photos, price, and contact details.
            """
        elif "ragging" in q_lower or "help" in q_lower:
             response = """
            🚨 **Anti-Ragging Helpline:** +91-1800-180-5522 (National)
            For campus issues, contact the Anti-Ragging Squad directly (check the **College Contacts** section).
            """
        elif "pyq" in q_lower or "previous year question" in q_lower:
             response = """
            📚 **Accessing PYQs (Previous Year Questions):**
            PYQs are available through the **Academic Resources** section. Look for the "Question Papers" section or check the drive links shared by your course coordinator.
            """
        elif "teacher" in q_lower or "professor" in q_lower:
            response = "Teacher contacts are available in **College Contacts** section."
        elif "secretary" in q_lower or "gymkhana" in q_lower:
            response = "Gymkhana secretary contacts are listed in **College Contacts** section."
        elif "opportunity" in q_lower or "update" in q_lower:
            response = "Check **Opportunities & Updates** section for latest info."
        
        # Add the new chat entry to history
        st.session_state['chat_history'].append({"user": query, "bot": response})
        
        st.rerun() 

    # 5. Display chat history
    st.markdown("---")
    st.subheader("Chat History")
    for chat in st.session_state['chat_history']:
        st.write(f"🧑 **You:** {chat['user']}")
        st.write(f"🤖 **Bot:** {chat['bot']}")


def show_generic_feature(feature_name, filter_container):
    """Renders a placeholder for any non-specific feature."""
    
    filter_container.empty()
    
    st.title(f"ℹ️ Campus-Sarthi: {feature_name}")
    st.markdown("---")
    
    if feature_name in ["Notices / Events", "Opportunities & Updates"]:
        st.info(f"This is the active content area for **{feature_name}**. Latest real-time notices and updates would appear here.")
        st.subheader("Sample Content Area")
        st.write("Latest update: Inter-department football match rescheduled for Friday.")
    else:
        st.info(f"This is the placeholder content for **{feature_name}**. This feature is accessible to all users.")
        st.subheader("Implementation Details")
        st.write("This section would connect to a dedicated database or external API for content retrieval (e.g., today's menu, list of lost items, academic forms).")


def show():
    """Main application function, coordinating features and filters."""
    
    # 1. Main Navigation (Draws the App Title and Feature list once)
    selected_feature = draw_sidebar_navigation()
    
    # 2. Create a placeholder container for dynamic sidebar content (filters/etc)
    # This must be *after* the permanent navigation is drawn.
    filter_container = st.sidebar.empty() 
    
    # 3. Display Content based on selection
    if selected_feature == "Class Schedule":
        # Pass the sidebar object directly so filters can be rendered inside it
        show_schedule(st.sidebar) 
        
    elif selected_feature == "Chatbot":
        # Pass the empty container to show_chatbot_feature so it can be cleared
        show_chatbot_feature(filter_container)
        
    else:
        # All other features are generic placeholders and need the container cleared
        show_generic_feature(selected_feature, filter_container)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Campus-Sarthi App",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    # Start the application
    show()