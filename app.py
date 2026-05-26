import streamlit as st
import joblib
import re
import nltk

# Load saved model & vectorizer
model = joblib.load("resume_svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Preprocessing function
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Streamlit UI
st.title("📄 Resume Screening System")
resume_input = st.text_area("Paste the resume text here:")

if st.button("Predict Category"):
    if resume_input.strip():
        cleaned = clean_text(resume_input)
        features = vectorizer.transform([cleaned])
        prediction = model.predict(features)
        st.success(f"Predicted Category: **{prediction[0]}**")
    else:
        st.warning("Please enter some resume text.")

