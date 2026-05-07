import streamlit as st
from textblob import TextBlob
from music_data import MUSIC_DATABASE, MOOD_EMOJIS

# PAGE SETTINGS
st.set_page_config(
    page_title="Mood Music Recommender",
    page_icon="🎵",
    layout="centered"
)

# TITLE
st.title("🎵 Mood-Based Music Recommender")

st.write(
    "Enter how you are feeling and get music recommendations based on your mood."
)

# USER INPUT
user_text = st.text_area(
    "How are you feeling today?"
)

# MOOD DETECTION FUNCTION
def detect_mood(text):

    text = text.lower()

    # SADNESS
    sadness_words = [
        "sad", "cry", "depressed", "unhappy",
        "lonely", "heartbroken", "down",
        "upset", "not okay", "feeling low",
        "broken", "hurt", "bad"
    ]

    # ANGER
    anger_words = [
        "angry", "mad", "furious",
        "hate", "annoyed", "rage",
        "frustrated"
    ]

    # JOY
    joy_words = [
        "happy", "great", "awesome",
        "excited", "amazing", "good"
    ]

    # LOVE
    love_words = [
        "love", "romantic", "cute",
        "beautiful", "adore", "miss you"
    ]

    # FEAR
    fear_words = [
        "fear", "afraid", "scared",
        "anxious", "worried", "nervous"
    ]

    # SURPRISE
    surprise_words = [
        "wow", "surprised", "shocked",
        "unexpected", "omg"
    ]

    # KEYWORD CHECKING

    for word in sadness_words:
        if word in text:
            return "sadness"

    for word in anger_words:
        if word in text:
            return "anger"

    for word in joy_words:
        if word in text:
            return "joy"

    for word in love_words:
        if word in text:
            return "love"

    for word in fear_words:
        if word in text:
            return "fear"

    for word in surprise_words:
        if word in text:
            return "surprise"

    # TEXTBLOB FALLBACK

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0.5:
        return "joy"

    elif polarity > 0:
        return "love"

    elif polarity < -0.5:
        return "sadness"

    elif polarity < 0:
        return "anger"

    else:
        return "neutral"


# BUTTON
if st.button("🎶 Recommend Music"):

    if user_text.strip() == "":
        st.warning("Please enter your feelings.")

    else:

        mood = detect_mood(user_text)

        st.success(
            f"Detected Mood: {mood.upper()} {MOOD_EMOJIS[mood]}"
        )

        st.subheader("🎧 Recommended Songs")

        for song in MUSIC_DATABASE[mood]:

            st.write(
                f"🎵 {song['song']} — {song['artist']} ({song['year']})"
            )

        st.balloons()
