import streamlit as st
import pandas as pd
from datetime import datetime
import os

DATA_FILE = "notices_data.csv"
BANNERS_DIR = "banners"
ADMIN_PASSWORD = "campusadmin123"  # Set your own password

def show():
    st.header("📢 Notices & Events")

    # Check if admin
    st.sidebar.subheader("Admin Login (Optional)")
    password = st.sidebar.text_input("Enter Admin Password", type="password")
    is_admin = password == ADMIN_PASSWORD

    if is_admin:
        st.sidebar.success("✅ Admin mode enabled")

    # -----------------------------
    # Admin: Add New Event / Notice
    # -----------------------------
    if is_admin:
        st.subheader("Add New Event / Notice")
        event_name = st.text_input("Event / Notice Name *", key="admin_name")
        description = st.text_area("Description (Optional)", key="admin_desc")
        venue = st.text_input("Venue (Optional)", key="admin_venue")
        contact = st.text_input("Email / Phone (Optional)", key="admin_contact")
        banner = st.file_uploader("Upload Banner (Optional)", type=['png', 'jpg', 'jpeg'], key="admin_banner")
        date = st.date_input("Event Date (Optional)", key="admin_date")

        if st.button("Add Event / Notice"):
            if event_name.strip() == "":
                st.warning("Event / Notice Name is required!")
            else:
                # Prepare data row
                data = {
                    "Name": event_name,
                    "Description": description,
                    "Venue": venue,
                    "Contact": contact,
                    "Date": date.strftime("%d-%m-%Y") if date else "",
                    "Banner": banner.name if banner else ""
                }

                # Save banner
                if banner:
                    os.makedirs(BANNERS_DIR, exist_ok=True)
                    with open(f"{BANNERS_DIR}/{banner.name}", "wb") as f:
                        f.write(banner.getbuffer())

                # Append to CSV
                if os.path.exists(DATA_FILE):
                    df = pd.read_csv(DATA_FILE)
                    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
                else:
                    df = pd.DataFrame([data])
                df.to_csv(DATA_FILE, index=False)
                st.success(f"✅ '{event_name}' added successfully!")

    # -----------------------------
    # Display Existing Notices / Events
    # -----------------------------
    st.subheader("Existing Notices / Events")
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        for idx, row in df.iterrows():
            st.markdown(f"### {row['Name']}")
            if row['Description']:
                st.markdown(f"**Description:** {row['Description']}")
            if row['Venue']:
                st.markdown(f"**Venue:** {row['Venue']}")
            if row['Contact']:
                st.markdown(f"**Contact:** {row['Contact']}")
            if row['Date']:
                st.markdown(f"**Date:** {row['Date']}")

            # Only show banner if it exists
            if pd.notna(row['Banner']) and row['Banner'].strip() != "":
                banner_path = f"{BANNERS_DIR}/{row['Banner']}"
                if os.path.exists(banner_path):
                    st.image(banner_path, caption=row['Banner'], use_container_width=True)
            st.markdown("---")

        # -----------------------------
        # Admin: Remove Event / Notice
        # -----------------------------
        if is_admin:
            st.subheader("🗑 Remove Event / Notice (Admin Only)")
            notice_to_remove = st.selectbox("Select Notice to Remove", df['Name'])
            if st.button("Remove Selected Notice"):
                df = df[df['Name'] != notice_to_remove]
                df.to_csv(DATA_FILE, index=False)
                st.success(f"❌ '{notice_to_remove}' removed successfully!")

                # -----------------------------
                # Streamlit rerun fix
                # -----------------------------
                try:
                    st.experimental_rerun()  # For older versions
                except AttributeError:
                    from streamlit.runtime.scriptrunner.script_runner import RerunException
                    from streamlit.runtime.scriptrunner.script_runner import add_script_run_ctx
                    raise RerunException(st.session_state)  # Force rerun
