import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import re

st.set_page_config(page_title="CV Prompt Generator Access", layout="centered")
st.title("🔐 Confirm Email to Access CV Generator")

# Session state
if "access_granted" not in st.session_state:
    st.session_state.access_granted = False
if "generated_prompt" not in st.session_state:
    st.session_state.generated_prompt = ""

# Google Sheets auth
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
try:
    creds = Credentials.from_service_account_info(
        st.secrets["google_service_account"], scopes=scope
    )
    client = gspread.authorize(creds)
    sheet = client.open("CVPromptEmails").sheet1
except Exception:
    st.error("⚠️ Could not authenticate or access the email list. Please contact support.")
    st.stop()

# Email access
if not st.session_state.access_granted:
    email_input = st.text_input("Enter the email you used after payment")

    if st.button("Access Generator"):
        if not email_input:
            st.warning("Please enter your email.")
        else:
            email_input = email_input.strip().lower()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email_input):
                st.warning("Please enter a valid email address.")
            else:
                try:
                    emails = [e.lower() for e in sheet.col_values(1)]
                except Exception:
                    st.error("⚠️ Could not fetch email list from the spreadsheet.")
                    st.stop()

                if email_input in emails:
                    st.session_state.access_granted = True
                    st.success("✅ Access granted!")
                else:
                    st.error("❌ Email not found. Please make sure you entered the correct email.")

# Prompt Generator
if st.session_state.access_granted:
    st.markdown("### 🔍 Job Description → CV Prompt Generator")
    st.write("Craft better prompts to optimize your CV for the job — without sounding like a robot.")

    job_description = st.text_area("📄 Paste the job description", height=300)
    user_cv = st.text_area("👤 Paste a short version of your CV or background", height=200)

    if st.button("✍️ Generate Prompt"):
        if not job_description or not user_cv:
            st.warning("Please fill in both the job description and your CV.")
        else:
            prompt_template = st.secrets["prompt"]["cv_rewrite"]
            st.session_state.generated_prompt = prompt_template.format(
                job_description=job_description,
                user_cv=user_cv
            )

    if st.session_state.generated_prompt:
        st.subheader("🎯 AI Prompt You Can Use")
        st.code(st.session_state.generated_prompt, language="markdown")

        st.markdown(
            '<p style="margin-top:1em;"><a href="https://chat.openai.com" target="_blank">🚀 Open ChatGPT to Paste This Prompt</a></p>',
            unsafe_allow_html=True
        )

    st.markdown("---")
