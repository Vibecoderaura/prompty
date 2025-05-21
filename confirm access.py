import streamlit as st

st.set_page_config(page_title="CV Prompt Generator", layout="centered")

st.title("🔍 Job Description → CV Prompt Generator")
st.write("Craft better prompts to optimize your CV for the job — without sounding like a robot.")

# User input
job_description = st.text_area("📄 Paste the job description", height=300)
user_cv = st.text_area("👤 Paste a short version of your CV or background", height=200)

# Generate prompt
if st.button("✍️ Generate Prompt"):
    if not job_description or not user_cv:
        st.warning("Please fill in both the job description and your CV.")
    else:
        prompt = f"""You are a professional resume writer. Based on the job description below and the candidate's background, tailor the CV to highlight the most relevant experiences and skills, making it ATS-friendly while sounding natural and human, not just copying the job description, not using 4 or more words next to each other in the job description directly in the CV, no long dashes and not overly AI-written or generic.

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

Return the full revised CV."""

        st.subheader("🎯 AI Prompt You Can Use")
        st.markdown("**📋 To use this prompt:**")
        st.markdown("""
        1. Highlight the full prompt below with your mouse.
        2. Right-click and select **Copy** (or press `Ctrl+C` / `Cmd+C`).
        3. [Click here to open ChatGPT](https://chat.openai.com) and paste it in.
        """)
        st.code(prompt, language="markdown")

st.markdown("---")
