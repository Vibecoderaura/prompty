import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="CV Prompt Generator – Subscribe", page_icon="📝", layout="centered")

st.title("📝 Unlock the CV Prompt Generator")

st.markdown("""
## Get naturally worded, professional CV prompts.

**What you get**:
- Custom prompts for ChatGPT or other AI tools
- Human-sounding, well-structured suggestions
- Tailored for your background and job description

---

### 💳 Access Details

- **Price**: £2.99 (30-day access)
- **Secure Payment**: PayPal (card payments accepted)
- **Delivery**: You’ll be taken to the next step right after payment

---

### 👇 Click Below to Pay & Proceed
""")

# Replace this link with your actual PayPal *business* payment link that redirects to App 2
paypal_link = "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YOUR_BUTTON_ID"

st.markdown(f"""
[🔐 Pay £2.99 and Continue]({paypal_link})
""")

st.markdown("""
---

### ✅ After Payment
You’ll be redirected to a page where you:
1. Enter your email to activate access
2. Get a link to the CV Prompt Generator
3. Must save/bookmark the link for future use

---

If you encounter issues, email **frankohemeng@googlemail.com** with your PayPal receipt.
""")

