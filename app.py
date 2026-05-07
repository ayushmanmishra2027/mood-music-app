# app.py

from music_data import MUSIC_DATABASE, MOOD_EMOJIS

def show_moods():
    print("\nAvailable moods:")
    for mood in MUSIC_DATABASE:
        print(f"{MOOD_EMOJIS[mood]} {mood}")

def recommend_music(mood):
    if mood not in MUSIC_DATABASE:
        print("\nInvalid mood! Try again.")
        return

    print(f"\nSongs for {mood.upper()} {MOOD_EMOJIS[mood]}:\n")

    for song in MUSIC_DATABASE[mood]:
        print(f"- {song['song']} by {song['artist']} ({song['year']})")

def main():
    print("🎵 Mood-Based Music Recommender 🎵")

    while True:
        show_moods()
        user_mood = input("\nEnter your mood (or 'exit' to quit): ").lower()

        if user_mood == "exit":
            print("\nGoodbye!")
            break

        recommend_music(user_mood)

if __name__ == "__main__":
    main()
