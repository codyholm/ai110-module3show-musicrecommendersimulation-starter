"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Default profile for a bright, energetic pop listener.
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "target_tempo_bpm": 120,
        "target_acousticness": 0.2,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nDefault profile: pop / happy\n")
    print("Top recommendations:\n")

    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"   Score:   {score:.2f}")
        print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
