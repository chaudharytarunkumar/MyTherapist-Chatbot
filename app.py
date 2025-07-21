import streamlit as st
from textblob import TextBlob
from transformers import pipeline
import random

# Load HuggingFace sentiment classifier
classifier = pipeline("sentiment-analysis")

# Emotion keyword mapping
emotion_keywords = {
    "anxiety": ["anxious", "nervous", "worried", "panic", "uneasy", "restless"],
    "sadness": ["sad", "down", "cry", "lost", "depressed", "grief"],
    "anger": ["angry", "mad", "furious", "irritated", "hate", "rage"],
    "feeling low": ["tired", "worthless", "weak", "exhausted", "burnt out", "helpless"],
    "happy": ["happy", "joy", "cheerful", "great", "excited"],
    "glad": ["glad", "relieved", "thankful", "grateful", "satisfied"],
    "sorry": ["sorry", "guilt", "regret", "ashamed", "apologize"]
}

# Empathetic responses
emotion_responses = {
    "anxiety": "It’s okay to feel anxious. Let's try to breathe together. I'm here with you 🤝",
    "sadness": "I'm so sorry you're feeling this way. Would you like to talk more about it? 😢",
    "anger": "Your anger is valid. Want to vent a little more? I'm listening. 😡",
    "feeling low": "You might be feeling overwhelmed. Please remember that rest is okay. 🌙",
    "happy": "That's amazing to hear! I'm smiling with you! 😊",
    "glad": "I'm glad you're feeling good. Keep that positivity going 🌟",
    "sorry": "It's good that you care. Want to talk about what’s making you feel this way? 🫂",
    "default": "I'm here to listen. Please tell me more."
}

# Motivational quotes
quotes = [
    "You are stronger than you think.",
    "This too shall pass.",
    "You are not alone.",
    "Keep breathing. You got this.",
    "Feelings are just visitors. Let them come and go.",
    "Your mental health matters. Always."
]

# Detect emotion from keywords
def detect_emotion(user_input):
    input_lower = user_input.lower()
    for emotion, keywords in emotion_keywords.items():
        if any(kw in input_lower for kw in keywords):
            return emotion
    return "default"

# Generate chatbot reply
def get_bot_reply(user_input):
    emotion = detect_emotion(user_input)
    sentiment = TextBlob(user_input).sentiment.polarity
    ai_sentiment = classifier(user_input)[0]['label']

    if emotion != "default":
        return emotion_responses[emotion]
    elif ai_sentiment == "NEGATIVE":
        return "You seem a bit off today. I'm right here if you need to talk. 🫂"
    elif ai_sentiment == "POSITIVE":
        return "That's lovely to hear! Keep smiling 😄"
    else:
        return emotion_responses["default"]

# Streamlit UI
st.set_page_config(page_title="MyTherapist Chatbot", layout="centered")
st.title("🧠 MyTherapist - Your Mental Health Chatbot")
st.markdown("Hi! I'm here to support you emotionally. Just type how you're feeling.")

user_input = st.text_input("Type your message here:")

if user_input:
    response = get_bot_reply(user_input)
    st.markdown(f"**🧠 Therapist:** {response}")

st.markdown("---")
st.subheader("💡 Today's Quote:")
st.info(random.choice(quotes))
