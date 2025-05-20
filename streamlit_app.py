import streamlit as st

st.set_page_config(page_title="CV Prompt Generator – Subscribe", page_icon="📝", layout="centered")

st.title("📝 Unlock the CV Prompt Generator")

st.markdown("""
## Get naturally worded, professional CV prompts.

**What you get**:
- Prompts that sound **human-written**, not AI-generated
- Well-structured, professional tone
- Tailored for your experience and job description
- Works perfectly with ChatGPT or other AI tools

---

### 💳 Access Details

- **Price**: £2.99 for 30 days access
- **Payment method**: PayPal (card accepted)
- **Next step**: After payment, you’ll be redirected to enter your email to activate access

---
""")

# Insert your working PayPal link
paypal_button_url = "https://www.paypal.com/ncp/payment/WANYK2SZLQ9UG"

st.markdown(f"""
## 👉 [Click here to pay £2.99 and continue]({paypal_button_url})
""", unsafe_allow_html=True)

st.markdown("""
---

### 🔄 After Payment:
1. You'll be **redirected to a form** to enter your email address.
2. Once submitted, you’ll receive instant access to the prompt generator.
3. You can **save the generator link** and reuse it for 30 days.

---

If anything goes wrong, email: **frankohemeng@googlemail.com**
""")
