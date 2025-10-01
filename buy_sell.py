import streamlit as st
import pandas as pd
import os
from datetime import datetime
import uuid

# File to store buy & sell data
FILE_PATH = "buy_sell.csv"
IMAGE_FOLDER = "buy_sell_images"

# Ensure image folder exists
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# Load existing data from CSV
def load_items():
    if os.path.exists(FILE_PATH):
        try:
            df = pd.read_csv(FILE_PATH)
            df = df.fillna("")  # Replace NaN with empty string
            return df.to_dict(orient="records")
        except pd.errors.EmptyDataError:
            return []
    return []

# Save data to CSV
def save_items(items):
    df = pd.DataFrame(items)
    df.to_csv(FILE_PATH, index=False)

def show():
    st.title("🛒 Buy & Sell")

    items = load_items()

    # ---------------- Add Item Section ----------------
    st.subheader("➕ Add Item for Buy/Sell")
    with st.form("add_item_form", clear_on_submit=True):
        item_name = st.text_input("Item Name (required)")
        description = st.text_area("Description (required)")
        price = st.text_input("Price (required, numeric)")
        contact = st.text_input("Email / Phone (required)")
        image_file = st.file_uploader("Upload Item Image (optional)", type=["jpg", "jpeg", "png"])
        submit = st.form_submit_button("Add Item")

        if submit:
            # Backend validation
            if not item_name.strip():
                st.warning("⚠️ Item Name is required.")
            elif not description.strip():
                st.warning("⚠️ Description is required.")
            elif not price.strip() or not price.strip().isdigit():
                st.warning("⚠️ Price is required and must be numeric.")
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
                    "ID": str(uuid.uuid4()),
                    "ItemName": item_name.strip(),
                    "Description": description.strip(),
                    "Price": price.strip(),
                    "Contact": contact.strip(),
                    "Image": image_path
                }
                items.append(new_item)
                save_items(items)
                st.success("✅ Item added successfully!")

    # ---------------- Display Items ----------------
    st.subheader("📋 Items for Sale / Wanted")
    if items:
        for item in items:
            st.write(f"**Item:** {item['ItemName']}")
            st.write(f"**Description:** {item['Description']}")
            st.write(f"**Price:** {item['Price']}")
            st.write(f"📞 {item['Contact']}")
            if item.get("Image") and isinstance(item["Image"], str) and os.path.exists(item["Image"]):
                st.image(item["Image"], width=200)
            st.markdown("---")
    else:
        st.info("No items listed yet.")

    # ---------------- Remove Item Section ----------------
    st.subheader("❌ Remove Your Item")
    with st.form("remove_item_form"):
        contact_input = st.text_input("Enter Your Contact Info (must match submission)")
        remove_btn = st.form_submit_button("Remove Item")

        if contact_input.strip():
            user_items = [i for i in items if str(i["Contact"]).strip().lower() == str(contact_input).strip().lower()]

            if user_items:
                options = {f"{i['ItemName']} | {i['Price']}": i["ID"] for i in user_items}
                selected_item = st.selectbox("Select Item to Remove", list(options.keys()))

                if remove_btn:
                    selected_id = options[selected_item]
                    items = [i for i in items if i["ID"] != selected_id]
                    save_items(items)

                    # Remove image if exists
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
                st.info("No items found for this contact info.")