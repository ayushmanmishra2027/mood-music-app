import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

from music_data import MUSIC_DATABASE, MOOD_EMOJIS

# PAGE CONFIG
st.set_page_config(
    page_title="Mood Music Recommender",
    page_icon="🎵",
    layout="centered"
)

# TITLE
st.title("🎵 AI Mood-Based Music Recommender")

st.write(
    "Enter your feelings and get music recommendations using AI."
)

# TRAINING DATA
training_data = {
    "text": [
        "I am very happy",
        "Life is amazing",
        "I feel awesome",
        "I love everyone",
        "You are beautiful",
        "I miss her",
        "I feel sad",
        "I am broken",
        "Feeling lonely",
        "I want to cry",
        "I hate this",
        "I am angry",
        "This is frustrating",
        "I feel nervous",
        "I am scared",
        "I am worried",
        "Wow amazing surprise",
        "OMG unbelievable",
        "Nothing special today",
        "I am okay"
    ],

    "mood": [
        "joy",
        "joy",
        "joy",
        "love",
        "love",
        "love",
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "anger",
        "anger",
        "anger",
        "fear",
        "fear",
        "fear",
        "surprise",
        "surprise",
        "neutral",
        "neutral"
    ]
}

# CREATE DATAFRAME
df = pd.DataFrame(training_data)

# SVM MACHINE LEARNING MODEL
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", SVC(kernel='linear'))
])

# TRAIN MODEL
model.fit(df["text"], df["mood"])

# USER INPUT
user_text = st.text_area(
    "How are you feeling today?"
)

# BUTTON
if st.button("🎶 Recommend Music"):

    if user_text.strip() == "":
        st.warning("Please enter your feelings.")

    else:

        # PREDICT MOOD
        mood = model.predict([user_text])[0]

        # SHOW RESULT
        st.success(
            f"Detected Mood: {mood.upper()} {MOOD_EMOJIS[mood]}"
        )

        # RECOMMEND SONGS
        st.subheader("🎧 Recommended Songs")

        for song in MUSIC_DATABASE[mood]:

            st.write(
                f"🎵 {song['song']} — {song['artist']} ({song['year']})"
            )

        st.balloons()
