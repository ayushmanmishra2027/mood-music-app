# app.py (Updated with NLP)

from music_data import MUSIC_DATABASE, MOOD_EMOJIS
from transformers import pipeline

# 1. Load a pre-trained NLP emotion classification model.
# This model will analyze text and classify it into: sadness, joy, love, anger, fear, or surprise.
print("Loading NLP Sentiment Model... (this may take a moment on first run)")
emotion_classifier = pipeline(
    "text-classification", 
    model="bhadresh-savani/bert-base-uncased-emotion"
)

def show_moods():
    print("\nAvailable moods:")
    for mood in MUSIC_DATABASE:
        print(f"{MOOD_EMOJIS[mood]} {mood}")

def analyze_mood_with_nlp(user_input):
    """
    Uses NLP to detect the emotion of a given sentence.
    """
    user_input_clean = user_input.strip().lower()
    
    # If the user typed an exact key from the database, use it directly
    if user_input_clean in MUSIC_DATABASE:
        return user_input_clean
        
    # Otherwise, use NLP to analyze the sentence
    try:
        prediction = emotion_classifier(user_input)[0]
        detected_mood = prediction['label'] # e.g., 'sadness', 'joy'
        confidence = prediction['score']
        
        print(f"\n🤖 NLP detected mood: {detected_mood.upper()} (Confidence: {confidence:.2%})")
        return detected_mood
    except Exception as e:
        # Fallback to neutral if classification fails
        return "neutral"

def recommend_music(mood):
    if mood not in MUSIC_DATABASE:
        print("\nInvalid mood! Try again.")
        return

    print(f"\nSongs for {mood.upper()} {MOOD_EMOJIS[mood]}:\n")

    for song in MUSIC_DATABASE[mood]:
        print(f"- {song['song']} by {song['artist']} ({song['year']})")

def main():
    print("🎵 Mood-Based Music Recommender (Now Powered by NLP!) 🎵")

    while True:
        show_moods()
        user_input = input("\nHow are you feeling? (or type 'exit' to quit): ")

        if user_input.strip().lower() == "exit":
            print("\nGoodbye!")
            break

        # Use NLP to convert user's sentence into a structured mood
        detected_mood = analyze_mood_with_nlp(user_input)
        recommend_music(detected_mood)

if __name__ == "__main__":
    main()
