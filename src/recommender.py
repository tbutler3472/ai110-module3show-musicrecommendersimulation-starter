from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert their numeric fields."""
    import csv

    print(f"Loading songs from {csv_path}...")
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            row["energy"] = float(row["energy"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and explain its points."""
    genre_match = 1 if song["genre"] == user_prefs["genre"] else 0
    mood_match = 1 if song["mood"] == user_prefs["mood"] else 0
    energy_similarity = 1 - abs(song["energy"] - user_prefs["energy"])
    valence_preference = user_prefs.get("valence", 0.5)
    valence_similarity = 1 - abs(song["valence"] - valence_preference)

    genre_points = 30 * genre_match
    mood_points = 30 * mood_match
    energy_points = 20 * energy_similarity
    valence_points = 20 * valence_similarity
    score = genre_points + mood_points + energy_points + valence_points

    reasons = [
        f"genre {'match' if genre_match else 'mismatch'} (+{genre_points:.2f} points)",
        f"mood {'match' if mood_match else 'mismatch'} (+{mood_points:.2f} points)",
        f"energy similarity (+{energy_points:.2f} points)",
        f"valence similarity (+{valence_points:.2f} points)",
    ]

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by their recommendation scores."""
    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        recommendations.append((song, score, explanation))

    recommendations.sort(key=lambda recommendation: recommendation[1], reverse=True)
    return recommendations[:k]
