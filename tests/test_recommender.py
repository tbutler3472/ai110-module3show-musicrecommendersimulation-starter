from src.recommender import Song, UserProfile, Recommender, recommend_songs

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_recommend_songs_penalizes_artists_already_selected():
    user_prefs = {
        "genre": "rock",
        "mood": "happy",
        "energy": 0.8,
        "valence": 0.8,
    }
    songs = [
        {"id": 1, "artist": "Artist One", "genre": "rock", "mood": "happy", "energy": 0.8, "valence": 0.8},
        {"id": 2, "artist": "Artist One", "genre": "rock", "mood": "happy", "energy": 0.8, "valence": 0.65},
        {"id": 3, "artist": "Artist Two", "genre": "rock", "mood": "happy", "energy": 0.8, "valence": 0.5},
    ]

    results = recommend_songs(user_prefs, songs, k=3)

    assert [song["id"] for song, _, _ in results] == [1, 3, 2]
    assert results[1][1] == 94
    assert "diversity penalty (-15.00 points)" in results[2][2]


def test_recommend_songs_floors_scores_at_zero():
    user_prefs = {
        "genre": "rock",
        "mood": "happy",
        "energy": 0,
        "valence": 0,
    }
    songs = [
        {"id": 1, "artist": "Same Artist", "genre": "other", "mood": "sad", "energy": 0.8, "valence": 0.8},
        {"id": 2, "artist": "Same Artist", "genre": "other", "mood": "sad", "energy": 0.8, "valence": 0.8},
    ]

    results = recommend_songs(user_prefs, songs, k=2)

    assert results[1][1] == 0
    assert "diversity penalty (-15.00 points)" in results[1][2]
