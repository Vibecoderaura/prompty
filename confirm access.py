import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import re

st.set_page_config(page_title="CV Prompt Generator Access", layout="centered")
st.title("🔐 Confirm Email to Access CV Generator")

# Authenticate using Streamlit secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=scope)
client = gspread.authorize(creds)

try:
    sheet = client.open("CVPromptEmails").sheet1
except Exception as e:
    st.error("⚠️ Cannot access the email list. Contact support.")
    st.stop()

email_input = st.text_input("Enter the email you used after payment")

if st.button("Access Generator"):
    if email_input:
        email_input = email_input.strip().lower()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_input):
            st.warning("Please enter a valid email address.")
        else:
            emails = [e.lower() for e in sheet.col_values(1)]
            if email_input in emails:
                st.success("✅ Access granted!")
                st.markdown("### 🎯 CV Prompt Generator")

                job_title = st.text_input("Job Title")
                background = st.text_area("Your Professional Background")

                if st.button("Generate Prompt"):
                    st.write("Here's your custom prompt:")
                    st.code(f"Write a professional CV for a {job_title} based on the following background:\n{background}")
            else:
                st.error("❌ Email not found. Please make sure you entered the correct email.")
    else:
        st.warning("Please enter your email.")

