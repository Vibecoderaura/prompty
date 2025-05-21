import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Enter Email to Access CV Generator", layout="centered")
st.title("✅ Confirm Your Email")
st.write("Thanks for your payment! Please enter your email below to access the CV Generator.")

# Use secrets stored in Streamlit
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Use credentials directly from st.secrets
creds = Credentials.from_service_account_info(
    st.secrets["google_service_account"], scopes=scope
)

client = gspread.authorize(creds)

# Connect to your Google Sheet
sheet = client.open("CVPromptEmails").sheet1

email = st.text_input("Enter your email address")

if st.button("Continue"):
    if email:
        sheet.append_row([email])
        st.success("✅ Email saved.")
        st.markdown("➡️ [Click here to continue to the CV Generator](https://confirmation.streamlit.app/confirm_access)")
    else:
        st.warning("Please enter a valid email.")

