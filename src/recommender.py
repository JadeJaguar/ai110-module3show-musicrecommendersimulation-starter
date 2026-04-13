import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """A single song and its audio attributes loaded from the catalog CSV."""
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
    """A listener's taste preferences used to score songs against."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """OOP wrapper that holds the song catalog and exposes recommendation methods."""

    def __init__(self, songs: List[Song]):
        """Stores the song catalog for use in recommendation and explanation methods."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k Song objects ranked by score against the given user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a plain-English explanation of why a song was recommended to a user."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads a CSV file and returns a list of song dicts with numeric fields cast to float/int."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores one song against user preferences (max 5.0) and returns the score plus a list of reasons."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append(f"genre match (+2.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append(f"mood match (+1.0)")

    energy_points = 1.0 - abs(song["energy"] - user_prefs["energy"])
    score += energy_points
    reasons.append(f"energy proximity (+{energy_points:.2f})")

    song_is_acoustic = song["acousticness"] > 0.5
    if song_is_acoustic == user_prefs.get("likes_acoustic", True):
        score += 1.0
        reasons.append(f"acoustic preference match (+1.0)")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song in the catalog and returns the top k as (song, score, explanation) tuples."""
    results = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = " | ".join(reasons)
        results.append((song, score, explanation))

    results.sort(key=lambda t: t[1], reverse=True)
    return results[:k]
