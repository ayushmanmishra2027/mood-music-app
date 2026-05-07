import streamlit as st
# app.py (ML-Based Mood Detection using Naive Bayes)

```python
import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from music_data import MUSIC_DATABASE, MOOD_EMOJIS

# PAGE CONFIG
st.set_page_config(
    page_title="Mood Music Recommender",
    page_icon="🎵",
    layout="centered"
)

# TITLE
st.title("🎵 Mood-Based Music Recommender")

st.write(
    "Enter your feelings and get music recommendations based on AI mood detection."
)

# TRAINING DATASET
training_data = {
    "text": [
        "I am very happy",
        "Life is amazing",
        "I feel awesome",
        "I love everyone",
        "I miss her",
        "You are beautiful",
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
        "Wow this is shocking",
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

# MACHINE LEARNING PIPELINE
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# TRAIN MODEL
model.fit(df['text'], df['mood'])

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

        # SHOW DETECTED MOOD
        st.success(
            f"Detected Mood: {mood.upper()} {MOOD_EMOJIS[mood]}"
        )

        # SHOW SONGS
        st.subheader("🎧 Recommended Songs")

        for song in MUSIC_DATABASE[mood]:

            st.write(
                f"🎵 {song['song']} — {song['artist']} ({song['year']})"
            )

        st.balloons()
```

---

# requirements.txt

```txt
streamlit
textblob
scikit-learn
pandas
```

---

# Core ML Concepts Used

## 1. CountVectorizer

Converts text into numerical vectors.

Example:

```text
"I am happy"
```

becomes:

```text
[0,1,0,1,1]
```

Machine learning models cannot understand text directly, so vectorization converts words into numbers.

---

## 2. Multinomial Naive Bayes

A machine learning classification algorithm.

Used for:

* Sentiment analysis
* Spam detection
* Text classification

It predicts mood based on probability of words.

Example:

Words like:

* happy
* awesome
* amazing

increase probability of:

```text
joy
```

---

## 3. Pipeline

Combines:

* CountVectorizer
* Naive Bayes model

into one system.

```python
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
```

---

## 4. Model Training

```python
model.fit(df['text'], df['mood'])
```

This teaches the AI model patterns between:

* text
* mood labels

---

## 5. Prediction

```python
model.predict([user_text])[0]
```

Predicts user emotion using trained ML model.

---

# Presentation Line

“We upgraded the project from basic sentiment analysis to a machine learning-based recommendation system using CountVectorizer and Multinomial Naive Bayes. The model is trained on sample emotional text data and predicts user mood more intelligently before recommending songs.”
