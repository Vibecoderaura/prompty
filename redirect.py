import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Enter Email to Access CV Generator", layout="centered")

st.title("✅ Confirm Your Email")

st.write("Thanks for your payment! Please enter your email below to access the CV Generator.")

# Authenticate Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
client = gspread.authorize(creds)

# Connect to the Google Sheet (update name to match yours)
sheet = client.open("CVPromptEmails").sheet1  # Make sure this Sheet exists

email = st.text_input("Enter your email address")

if st.button("Continue"):
    if email:
        sheet.append_row([email])
        st.success("✅ Email saved. Redirecting you to the next page...")
        st.markdown(f"[Click here to continue](https://your-app-url/confirm_access)")
    else:
        st.warning("Please enter a valid email.")
