# chatbot.py
import streamlit as st

def show():
    """Main chatbot function"""
    st.title("🤖 Campus-Sarthi: Chatbot")
    st.markdown("Ask me about mess, classes, contacts, or anything campus related!")
    st.markdown("---")

    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Display chat history
    for message in st.session_state['chat_history']:
        role_label = message["role"] 
        with st.chat_message(role_label):
            st.markdown(message["content"])

    # Chat Input and Logic
    query = st.chat_input("Say something...")
    
    # Process Query and Update History
    if query:
        # Add and display user message immediately
        st.session_state['chat_history'].append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)
            
        # Determine Bot Response
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
        
        # Display and store bot response
        with st.chat_message("assistant"):
            st.markdown(response)
            
        st.session_state['chat_history'].append({"role": "assistant", "content": response})

# Run the app directly
if __name__ == "__main__":
    st.set_page_config(
        page_title="Campus-Sarthi Chatbot",
        page_icon="🤖",
        layout="centered"
    )
    show()