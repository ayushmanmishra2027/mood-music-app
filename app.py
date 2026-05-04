# app.py

import streamlit as st
from music_data import MUSIC_DATABASE, MOOD_EMOJIS

st.title("🎵 Mood-Based Music Recommender")

mood = st.selectbox("Choose your mood:", list(MUSIC_DATABASE.keys()))

if st.button("Get Songs"):
    st.subheader(f"{MOOD_EMOJIS[mood]} {mood.upper()}")

    for song in MUSIC_DATABASE[mood]:
        st.write(f"🎶 {song['song']} - {song['artist']} ({song['year']})")
