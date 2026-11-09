import streamlit as st
import pickle
import time

# 1. Page Configuration (yeh sabse pehli line honi chahiye)
st.set_page_config(page_title="Email Threat Analyzer", page_icon="🛡️", layout="centered")

# Model aur Vectorizer load karo
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# 2. Professional Header & Subtitle
st.markdown("<h1 style='text-align: center;'>🛡️ Email Threat Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Paste the suspicious email content below to check for spam or phishing indicators.</p>", unsafe_allow_html=True)
st.divider() 

# 3. Bada aur clean Text Area
user_email = st.text_area("EMAIL Content", height=200, placeholder="Paste the email text here...")

# 4. Full-width Button
if st.button('Analyze EMAIL', use_container_width=True):
    if user_email.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        # Loading effect ke liye spinner
        with st.spinner("Analyzing text patterns and linguistic markers..."):
            time.sleep(1) # Realistic feel ke liye halka sa delay
            
            # Predict
            email_tfidf = tfidf.transform([user_email])
            prediction = model.predict(email_tfidf)
            
            # 5. Clean Results
            st.divider()
            if prediction[0] == 1:
                st.error("🚨 **HIGH RISK DETECTED**\n\nThis message exhibits strong spam/phishing characteristics. Avoid clicking any links or sharing sensitive information.")
            else:
                st.success("✅ **SAFE**\n\nNo significant spam indicators found. The message appears to be legitimate.")