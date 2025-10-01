import streamlit as st
import pandas as pd
import os
from datetime import datetime
import uuid

# File to store lost & found data
FILE_PATH = "lost_found.csv"
IMAGE_FOLDER = "lost_found_images"

# Ensure image folder exists
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# Load existing data from CSV
def load_items():
    if os.path.exists(FILE_PATH):
        try:
            df = pd.read_csv(FILE_PATH)
            df = df.fillna("")  # Replace NaN with empty string to avoid TypeError
            return df.to_dict(orient="records")
        except pd.errors.EmptyDataError:
            return []
    return []

# Save data to CSV
def save_items(items):
    df = pd.DataFrame(items)
    df.to_csv(FILE_PATH, index=False)

def show():
    st.title("📦 Lost & Found")

    items = load_items()

    # ---------------- Add Item Section ----------------
    st.subheader("➕ Add Lost/Found Item")
    with st.form("add_item_form", clear_on_submit=True):
        name = st.text_input("Your Name (optional)")
        contact = st.text_input("Email / Phone (required)")
        description = st.text_area("Item Description (required)")
        status = st.selectbox("Status", ["Lost", "Found"])
        image_file = st.file_uploader("Upload Item Image (optional)", type=["jpg", "jpeg", "png"])
        submit = st.form_submit_button("Add Item")

        if submit:
            # Backend validation
            if not description.strip():
                st.warning("⚠️ Description is required.")
            elif not contact.strip():
                st.warning("⚠️ Contact is required.")
            else:
                image_path = ""
                if image_file:
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    image_path = os.path.join(IMAGE_FOLDER, f"{timestamp}_{image_file.name}")
                    with open(image_path, "wb") as f:
                        f.write(image_file.getbuffer())

                new_item = {
                    "ID": str(uuid.uuid4()),  # unique ID
                    "Name": name.strip(),     # optional
                    "Contact": str(contact.strip()),
                    "Description": description.strip(),
                    "Status": status,
                    "Image": image_path       # optional
                }
                items.append(new_item)
                save_items(items)
                st.success("✅ Item added successfully!")

    # ---------------- Display Items ----------------
    st.subheader("📋 Lost & Found Board")
    if items:
        for item in items:
            st.write(f"**Status:** {item['Status']}")
            st.write(f"**Description:** {item['Description']}")
            contact_info = f"👤 {item['Name']} | 📞 {item['Contact']}" if item['Name'] else f"📞 {item['Contact']}"
            st.write(contact_info)

            # Safe image display
            if item.get("Image") and isinstance(item["Image"], str) and os.path.exists(item["Image"]):
                st.image(item["Image"], width=200)
            st.markdown("---")
    else:
        st.info("No items added yet.")

    # ---------------- Remove Item Section ----------------
    st.subheader("❌ Remove Your Item (if recovered)")
    with st.form("remove_item_form"):
        contact_input = st.text_input("Enter Your Contact Info (must match submission)")
        remove_btn = st.form_submit_button("Remove Item")

        if contact_input.strip():  # Proceed only if contact info entered
            # Filter items using case-insensitive match
            user_items = [
                i for i in items
                if str(i["Contact"]).strip().lower() == str(contact_input).strip().lower()
            ]

            if user_items:
                # Map descriptions to IDs
                options = {f"{i['Description']} ({i['Status']})": i["ID"] for i in user_items}
                selected_desc = st.selectbox("Select Item to Remove", list(options.keys()))

                if remove_btn:
                    selected_id = options[selected_desc]
                    # Remove the item with this ID
                    items = [j for j in items if j["ID"] != selected_id]
                    save_items(items)

                    # Also remove image if exists
                    for i in user_items:
                        if i["ID"] == selected_id and i.get("Image") and isinstance(i["Image"], str) and os.path.exists(i["Image"]):
                            os.remove(i["Image"])

                    st.success("✅ Item removed successfully!")

                    # Streamlit rerun fix
                    try:
                        st.experimental_rerun()
                    except AttributeError:
                        from streamlit.runtime.scriptrunner.script_runner import RerunException
                        from streamlit.runtime.scriptrunner.script_runner import add_script_run_ctx
                        raise RerunException(st.session_state)
            else:
                st.info("No items found for this contact info. Check for typos or formatting.")
