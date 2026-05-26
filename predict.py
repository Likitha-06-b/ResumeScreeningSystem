import joblib
import re

# ----------------------
# Preprocessing function
# ----------------------
def clean_text(text):
    text = re.sub(r"http\S+", " URL ", text)   # replace URLs with placeholder
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)  # keep numbers and letters
    text = text.lower()
    return text

# ----------------------
# Load model & vectorizer
# ----------------------
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ----------------------
# Prediction function
# ----------------------
def predict_news(news_text):
    news_text = clean_text(news_text)  
    news_vec = vectorizer.transform([news_text])
    prediction = model.predict(news_vec)[0]   # will return "real" or "fake"
    
    return "Real News" if prediction == "real" else "Fake News"

# ----------------------
# Repeated user input loop
# ----------------------
if __name__ == "__main__":
    print("Fake News Detector (type 'exit' to quit)\n")
    
    while True:
        news_input = input("Enter a news article/text: ")
        
        if news_input.strip().lower() in ["exit", "quit"]:
            print("\nExiting Fake News Detector. Goodbye!")
            break
        
        result = predict_news(news_input)
        print("Prediction:", result, "\n")

