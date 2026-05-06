import streamlit as st
from music_data import MUSIC_DATABASE, MOOD_EMOJIS

st.title("🎵 Mood-Based Music Recommender")

mood = st.selectbox(
    "Choose your mood:",
    list(MUSIC_DATABASE.keys())
)

if st.button("Recommend Songs"):

    st.subheader(f"Songs for {mood.upper()} {MOOD_EMOJIS[mood]}")

    for song in MUSIC_DATABASE[mood]:
        st.write(
            f"🎶 {song['song']} by {song['artist']} ({song['year']})"
        )
