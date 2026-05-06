import streamlit as st
from textblob import TextBlob
from music_data import MUSIC_DATABASE, MOOD_EMOJIS

st.title("🎵 Mood-Based Music Recommender")

user_text = st.text_area(
    "How are you feeling today?"
)

def detect_mood(text):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0.4:
        return "joy"

    elif polarity > 0:
        return "love"

    elif polarity < -0.4:
        return "sadness"

    elif polarity < 0:
        return "anger"

    else:
        return "neutral"

if st.button("Recommend Music"):

    if user_text.strip() == "":
        st.warning("Please enter your feelings.")
    else:

        mood = detect_mood(user_text)

        st.success(
            f"Detected Mood: {mood.upper()} {MOOD_EMOJIS[mood]}"
        )

        st.subheader("Recommended Songs")

        for song in MUSIC_DATABASE[mood]:

            st.write(
                f"🎶 {song['song']} by {song['artist']} ({song['year']})"
            )
