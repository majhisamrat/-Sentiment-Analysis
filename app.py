
import streamlit as st
import joblib

# Load model
model = joblib.load("sentiment_model.pkl")

st.title("🎬 IMDB Review Sentiment Analyzer")
st.write("Enter a movie review and get the sentiment result.")

# Input box
review = st.text_area("Enter your review here:")

# Predict
if st.button("Analyze"):
    prediction = model.predict([review])[0]
    st.subheader(f"🎯 Sentiment: **{prediction.upper()}**")

    if prediction == 'positive':
        st.success("😊 Positive")
    elif prediction == 'negative':
        st.error("😠 Negative")
    else:
        st.info("😐 Neutral")

