import streamlit as st

st.set_page_config(page_title="Professional CV Prompt Generator", page_icon="📝", layout="centered")

st.title("📝 CV Prompt Generator Access")

st.markdown("""
## Get a CV prompt that sounds **professional and human-written**, not like AI.

Avoid robotic, generic CVs. Our custom prompt generator creates:
- Naturally phrased, structured prompts
- Tailored to your background and the job description
- Ready to use with tools like ChatGPT to generate high-quality CV content

---

### 💳 Subscription Details

- **Price**: £2.99/month
- **Access**: Full access to the CV Prompt Generator
- **Delivery**: Once payment is confirmed, you'll receive access by email

---

### 🔒 Secure Payment via PayPal

To get started, click the button below to make your payment securely through PayPal.

**Important: Please include your email address in the "Notes" section of the PayPal form**  
This is how we verify your purchase and send you access.

""")

# Replace this with your actual PayPal.me link or button link
paypal_link = "https://paypal.me/GuessTheObject/2.99"

st.markdown(f"""
[👉 Click here to pay £2.99 via PayPal]({paypal_link})
""")

st.markdown("""
---

### 📩 What happens next?

1. You’ll receive a confirmation from PayPal
2. We’ll verify your payment manually
3. You’ll get a personal email with your access link

_You’ll have access for 30 days. After that, you can repurchase if you want to continue using the service._

""")

st.info("If you don't receive access within 12 hours of payment, please email us at frankohemeng@googlemail.com")


