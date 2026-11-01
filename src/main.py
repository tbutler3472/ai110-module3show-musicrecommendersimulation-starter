"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs
from textwrap import wrap


def print_recommendation_table(recommendations: list) -> None:
    headers = ("Rank", "Song Title", "Artist", "Score", "Reasons")
    rows = []

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        rows.append(
            (
                str(rank),
                song["title"],
                song["artist"],
                f"{score:.2f} / 100",
                explanation,
            )
        )

    widths = [
        max(len(headers[0]), *(len(row[0]) for row in rows)),
        max(len(headers[1]), *(len(row[1]) for row in rows)),
        max(len(headers[2]), *(len(row[2]) for row in rows)),
        max(len(headers[3]), *(len(row[3]) for row in rows)),
        70,
    ]

    def border() -> str:
        return "+" + "+".join("-" * (width + 2) for width in widths) + "+"

    def format_row(values: tuple) -> str:
        return "| " + " | ".join(
            value.ljust(width) for value, width in zip(values, widths)
        ) + " |"

    print(border())
    print(format_row(headers))
    print(border())

    for row in rows:
        reason_lines = wrap(row[4], width=widths[4]) or [""]
        for line_number, reason_line in enumerate(reason_lines):
            values = row[:4] + (reason_line,) if line_number == 0 else ("", "", "", "", reason_line)
            print(format_row(values))
        print(border())


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
        print_recommendation_table(recommendations)
        print()


if __name__ == "__main__":
    main()
