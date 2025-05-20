import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="CV Prompt Generator Access", layout="centered")

st.title("🔐 Confirm Email to Access CV Generator")

# Authenticate Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("CVPromptEmails").sheet1

email_input = st.text_input("Enter the email you used after payment")

if st.button("Access Generator"):
    if email_input:
        emails = sheet.col_values(1)
        if email_input.strip().lower() in [e.lower() for e in emails]:
            st.success("✅ Access granted!")
            st.markdown("### 🎯 CV Prompt Generator")
            job_title = st.text_input("Job Title")
            background = st.text_area("Your Professional Background")
            if st.button("Generate Prompt"):
                st.write(f"Here's your custom prompt:")
                st.code(f"Write a professional CV for a {job_title} based on the following background:\n{background}")
        else:
            st.error("❌ Email not found. Please make sure you entered the correct email.")
    else:
        st.warning("Please enter your email.")
