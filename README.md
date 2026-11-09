# 🛡️ Email Threat Analyzer

A Machine Learning based web application built to detect whether an email is Spam (Threat) or Normal (Safe). 

## 🚀 Live Demo
[Click here to view the app](https://shashank-spam-email-detector.streamlit.app/)

## 🧠 Tech Stack Used
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-Learn (Logistic Regression)
- **NLP Technique:** TF-IDF Vectorization
- **Language:** Python

## ⚙️ How It Works
1. The user pastes the suspicious email text into the app.
2. The text is processed and converted into numerical features using a pre-trained TF-IDF vectorizer.
3. The Logistic Regression model predicts if the text exhibits spam characteristics.
4. The UI immediately displays a risk alert or safety confirmation.

## 📂 Project Files
- `app.py`: Main Streamlit application code.
- `model.pkl`: Saved Logistic Regression model.
- `vectorizer.pkl`: Saved TF-IDF vectorizer.
- `requirements.txt`: Required Python dependencies.
