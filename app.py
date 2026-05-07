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

        # JOY
        "I am happy",
        "Life is amazing",
        "I feel awesome",
        "I am excited",
        "This is wonderful",
        "I feel great",

        # LOVE
        "I love her",
        "You are beautiful",
        "I miss you",
        "Feeling romantic",
        "You are special",

        # SADNESS
        "I am sad",
        "I feel depressed",
        "I want to cry",
        "I feel lonely",
        "I am heartbroken",
        "I am not okay",
        "Feeling very bad",
        "I feel broken",
        "I am hurt",
        "very sad",
        "sad very much",
        "i m sad",
        "feeling low",

        # ANGER
        "I hate this",
        "I am angry",
        "This is frustrating",
        "I am mad",

        # FEAR
        "I am scared",
        "I feel nervous",
        "I am worried",
        "I am afraid",

        # SURPRISE
        "Wow unbelievable",
        "OMG shocking",
        "This is surprising",

        # NEUTRAL
        "I am okay",
        "Nothing special",
        "Normal day"
    ],

    "mood": [

        # JOY
        "joy",
        "joy",
        "joy",
        "joy",
        "joy",
        "joy",

        # LOVE
        "love",
        "love",
        "love",
        "love",
        "love",

        # SADNESS
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "sadness",
        "sadness",

        # ANGER
        "anger",
        "anger",
        "anger",
        "anger",

        # FEAR
        "fear",
        "fear",
        "fear",
        "fear",

        # SURPRISE
        "surprise",
        "surprise",
        "surprise",

        # NEUTRAL
        "neutral",
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
