import streamlit as st

st.set_page_config(page_title="CV Prompt Generator", layout="centered")

st.title("🔍 Job Description → CV Prompt Generator")
st.write("Craft a strong AI prompt to tailor your CV to the job — without sounding robotic or using a soup of jargon.")

# --- Inputs ---
job_description = st.text_area("📄 Paste the job description", height=300)
user_cv = st.text_area("👤 Paste a short version of your CV or background", height=200)

# --- Generate Prompt ---
if st.button("✍️ Generate Prompt"):
    if not job_description or not user_cv:
        st.warning("Please fill in both fields above.")
    else:
        prompt = f"""
You are a professional resume writer. Use the job description and the candidate’s background below to rewrite the CV so it aligns with the job, sounds professional,doesn't just match everything in the job description but uses actual things that support the description, doesn't use long dashes anywhere in the text and feels natural—not AI-generated.

Job Description:
\"\"\"{job_description}\"\"\"

Candidate Background:
\"\"\"{user_cv}\"\"\"

Instructions:
- Focus on matching relevant skills/keywords naturally.
- Emphasize achievements, not just responsibilities.
- Keep a human tone and avoid generic AI phrasing.
- Do NOT make up anything—use only provided details.

Return the full rewritten CV.
"""
        st.subheader("🎯 Copy this Prompt")
        st.code(prompt, language="markdown")
        st.success("Copy the above and paste it into ChatGPT, Claude, etc.")

st.markdown("---")
st.caption("🚀 Made with Streamlit in GitHub Codespaces")
