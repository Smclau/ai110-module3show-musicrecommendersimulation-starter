"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from tabulate import tabulate
from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "Chill Lofi Session": {
            "favorite_genre":      "lofi",
            "favorite_mood":       "chill",
            "target_energy":       0.38,
            "target_acousticness": 0.75,
        },
        "Focused Lofi Session": {
            "favorite_genre":      "lofi",
            "favorite_mood":       "focused",
            "target_energy":       0.42,
            "target_acousticness": 0.72,
        },
        "Relaxed Lofi Session": {
            "favorite_genre":      "lofi",
            "favorite_mood":       "relaxed",
            "target_energy":       0.34,
            "target_acousticness": 0.82,
        },
        "Pop Happy Session": {
            "favorite_genre":      "pop",
            "favorite_mood":       "happy",
            "target_energy":       0.80,
            "target_acousticness": 0.20,
        },
        "High-Energy Pop": {
            "favorite_genre":      "pop",
            "favorite_mood":       "energetic",
            "target_energy":       0.90,
            "target_acousticness": 0.08,
        },
        "Deep Intense Rock": {
            "favorite_genre":      "rock",
            "favorite_mood":       "intense",
            "target_energy":       0.92,
            "target_acousticness": 0.10,
        },
        "Sad Acoustic Folk": {
            "favorite_genre":      "folk",
            "favorite_mood":       "sad",
            "target_energy":       0.30,
            "target_acousticness": 0.90,
        },
    }

    for profile_name, user_prefs in profiles.items():
        for strategy in ["energy-first", "genre-first", "mood-first"]:
            recommendations = recommend_songs(user_prefs, songs, k=5, strategy=strategy)
            print(f"\n{'='*65}")
            print(f"  {profile_name}  [{strategy}]")
            print(f"{'='*65}")
            rows = [
                [rank, song["title"], song["artist"], f"{score:.2f}", explanation]
                for rank, (song, score, explanation) in enumerate(recommendations, 1)
            ]
            print(tabulate(rows, headers=["#", "Title", "Artist", "Score", "Why"], tablefmt="rounded_outline"))
            print()


if __name__ == "__main__":
    main()
