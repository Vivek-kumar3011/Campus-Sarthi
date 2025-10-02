import streamlit as st
import pandas as pd
import os

DATA_FILE = "opportunities_data.csv"
BANNERS_DIR = "opportunity_banners"
ADMIN_PASSWORD = "campusadmin123"  # Set your own password

def show():
    st.header("💼 Opportunities & Updates")

    # Admin login
    st.sidebar.subheader("Admin Login (Optional)")
    password = st.sidebar.text_input("Enter Admin Password", type="password")
    is_admin = password == ADMIN_PASSWORD
    if is_admin:
        st.sidebar.success("✅ Admin mode enabled")

    # -----------------------------
    # Admin: Add New Opportunity / Update
    # -----------------------------
    if is_admin:
        st.subheader("Add New Opportunity / Update")
        name = st.text_input("Opportunity / Update Name *", key="opp_name")
        description = st.text_area("Description (Optional)", key="opp_desc")
        category = st.selectbox("Category", ["Internship", "Open Source", "Placement", "Scholarship", "Quiz", "Other"], key="opp_cat")
        apply_link = st.text_input("Application / Reference Link (Optional)", key="opp_link")
        contact = st.text_input("Contact Email / Phone (Optional)", key="opp_contact")
        banner = st.file_uploader("Upload Banner (Optional)", type=['png', 'jpg', 'jpeg'], key="opp_banner")

        if st.button("Add Opportunity / Update"):
            if name.strip() == "":
                st.warning("Opportunity / Update Name is required!")
            else:
                data = {
                    "Name": name,
                    "Description": description,
                    "Category": category,
                    "Link": apply_link,
                    "Contact": contact,
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
                st.success(f"✅ '{name}' added successfully!")

    # -----------------------------
    # Display Existing Opportunities / Updates
    # -----------------------------
    st.subheader("Existing Opportunities / Updates")
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        for idx, row in df.iterrows():
            st.markdown(f"### {row['Name']}")
            st.markdown(f"**Category:** {row['Category']}")
            if pd.notna(row['Description']) and row['Description'].strip() != "":
                st.markdown(f"**Description:** {row['Description']}")
            if pd.notna(row['Link']) and row['Link'].strip() != "":
                st.markdown(f"[Apply / Reference Link]({row['Link']})")
            if pd.notna(row['Contact']) and row['Contact'].strip() != "":
                st.markdown(f"**Contact:** {row['Contact']}")
            # Banner handling
            if pd.notna(row['Banner']) and row['Banner'].strip() != "":
                banner_path = f"{BANNERS_DIR}/{row['Banner']}"
                if os.path.exists(banner_path):
                    st.image(banner_path, caption=row['Banner'], use_column_width=True)
            st.markdown("---")

        # -----------------------------
        # Admin: Remove Opportunity / Update
        # -----------------------------
        if is_admin:
            st.subheader("🗑 Remove Opportunity / Update (Admin Only)")
            opp_to_remove = st.selectbox("Select Opportunity to Remove", df['Name'])
            if st.button("Remove Selected Opportunity / Update"):
                df = df[df['Name'] != opp_to_remove]
                df.to_csv(DATA_FILE, index=False)
                st.success(f"❌ '{opp_to_remove}' removed successfully!")
                # Streamlit rerun fix
                try:
                    st.experimental_rerun()
                except AttributeError:
                    from streamlit.runtime.scriptrunner.script_runner import RerunException
                    from streamlit.runtime.scriptrunner.script_runner import add_script_run_ctx
                    raise RerunException(st.session_state)
