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

    profiles = [
        (
            "High-Energy Pop",
            {"genre": "pop", "mood": "happy", "energy": 0.90, "valence": 0.85},
        ),
        (
            "Chill Lofi",
            {"genre": "lofi", "mood": "chill", "energy": 0.35, "valence": 0.55},
        ),
        (
            "Intense Rock",
            {"genre": "rock", "mood": "intense", "energy": 0.95, "valence": 0.40},
        ),
    ]

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name}")
        print(
            "Preferences: "
            f"genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
            f"energy={user_prefs['energy']:.2f}, "
            f"valence={user_prefs['valence']:.2f}"
        )
        print("Top 5 recommendations:\n")
        for number, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{number}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f} / 100")
            print("   Reasons:")
            for reason in explanation.split("; "):
                print(f"   - {reason}")
        print()


if __name__ == "__main__":
    main()
