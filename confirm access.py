import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import re

st.set_page_config(page_title="CV Prompt Generator Access", layout="centered")
st.title("🔐 Confirm Email to Access CV Generator")

# Authenticate with Google Sheets using Streamlit secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
try:
    creds = Credentials.from_service_account_info(
        st.secrets["google_service_account"], scopes=scope
    )
    client = gspread.authorize(creds)
    sheet = client.open("CVPromptEmails").sheet1
except Exception as e:
    st.error("⚠️ Could not authenticate or access the email list. Please contact support.")
    st.stop()

# Email input
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
            except Exception as e:
                st.error("⚠️ Could not fetch email list from the spreadsheet.")
                st.stop()

            if email_input in emails:
                st.success("✅ Access granted!")
                st.markdown("### 🎯 CV Prompt Generator")
                st.write("Craft better prompts to optimize your CV for the job — without sounding like a robot.")

                job_description = st.text_area("📄 Paste the job description", height=300)
                user_cv = st.text_area("👤 Paste a short version of your CV or background", height=200)

                if st.button("✍️ Generate Prompt"):
                    if not job_description or not user_cv:
                        st.warning("Please fill in both the job description and your CV.")
                    else:
                        st.subheader("🎯 AI Prompt You Can Use")
                        prompt = f"""
You are a professional resume writer. Based on the job description below and the candidate's background, tailor the CV to highlight the most relevant experiences and skills, making it ATS-friendly while sounding natural and human, not just copying the job description, not using 4 or more words next to each other in the job description directly in the CV — not overly AI-written or generic.

Job Description:
\"\"\"{job_description}\"\"\"

Candidate Background:
\"\"\"{user_cv}\"\"\"

Instructions:
- Focus on matching language from the job description subtly.
- Highlight achievements over responsibilities.
- Use a professional tone that reflects the candidate's industry.
- Make the writing sound real and personal, not machine-generated.
- Do NOT fabricate anything; use only information from the CV.

Return the full revised CV.
"""
                        st.code(prompt, language="markdown")
                        st.success("Copy this prompt into ChatGPT, Claude, or your preferred AI!")

                st.markdown("---")
                
            else:
                st.error("❌ Email not found. Please make sure you entered the correct email.")

