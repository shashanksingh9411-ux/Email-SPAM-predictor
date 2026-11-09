import streamlit as st
import pickle
import time

st.set_page_config(page_title="Email Threat Analyzer", page_icon="🛡️", layout="centered")

# Model aur Vectorizer load karo
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Main Header
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🛡️ Email Threat Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 16px;'>Protect your inbox. Paste any suspicious email below for instant AI analysis.</p>", unsafe_allow_html=True)
st.divider() 

# Input Section
with st.container():
    user_email = st.text_area("📨 Message Content", height=200, placeholder="Dear customer, your account has been compromised. Click here to verify...")

if st.button('🔍 Analyze Message', use_container_width=True):
    if user_email.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing text patterns, links, and linguistic markers..."):
            time.sleep(1)
            
            email_tfidf = tfidf.transform([user_email])
            prediction = model.predict(email_tfidf)[0]
            probabilities = model.predict_proba(email_tfidf)[0]
            
            normal_prob = round(probabilities[0] * 100, 2)
            spam_prob = round(probabilities[1] * 100, 2)
            
            st.divider()
            st.subheader("📊 Analysis Results")
            
            # Metric Columns for Scores
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Spam Probability", value=f"{spam_prob}%")
            with col2:
                st.metric(label="Normal (Safe) Probability", value=f"{normal_prob}%")
            
            # Visual Result Alert
            if prediction == 1:
                st.error("🚨 **HIGH RISK DETECTED**")
                st.progress(int(spam_prob))
                st.markdown("> **Warning:** This message exhibits strong spam/phishing characteristics. Do not click on any links or download attachments.")
            else:
                st.success("✅ **SAFE MESSAGE**")
                st.progress(int(normal_prob))
                st.markdown("> **Status:** No significant spam indicators found. The message appears to be legitimate.")
            
            # Technical Details Expander
            with st.expander("🤖 How did the AI make this decision?"):
                st.write("The model analyzes specific keywords, sentence structures, and punctuation commonly used by scammers. It compares your text against thousands of known spam emails to calculate these probabilities.")