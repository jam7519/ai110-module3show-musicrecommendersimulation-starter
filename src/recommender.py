import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Song:
    """Represents a song and its musical attributes."""

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
    """Represents a user's music preferences."""

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Object-oriented implementation of the recommendation logic."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> float:
        """Calculate a weighted score for one Song object."""

        score = 0.0

        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0

        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0

        energy_difference = abs(song.energy - user.target_energy)
        score += max(0.0, 2.0 * (1.0 - energy_difference))

        if user.likes_acoustic:
            score += song.acousticness
        else:
            score += 1.0 - song.acousticness

        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs sorted from highest to lowest score."""

        ranked_songs = sorted(
            self.songs,
            key=lambda song: self._score(user, song),
            reverse=True,
        )

        return ranked_songs[:k]

    def explain_recommendation(
        self,
        user: UserProfile,
        song: Song,
    ) -> str:
        """Explain why a Song object was recommended."""

        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("matches your favorite genre")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("matches your favorite mood")

        energy_difference = abs(song.energy - user.target_energy)

        if energy_difference <= 0.2:
            reasons.append("has energy close to your target")

        if user.likes_acoustic and song.acousticness >= 0.5:
            reasons.append("has an acoustic sound you may enjoy")

        if not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append("has a less acoustic sound")

        if not reasons:
            reasons.append("has some musical features near your preferences")

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""

    songs = []

    with open(csv_path, mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }

            songs.append(song)

    return songs


def score_song(
    user_prefs: Dict,
    song: Dict,
) -> Tuple[float, List[str]]:
    """Score one song against a user's preferences."""

    score = 0.0
    reasons = []

    favorite_genre = user_prefs.get("genre", "").lower()
    favorite_mood = user_prefs.get("mood", "").lower()
    target_energy = float(user_prefs.get("energy", 0.5))

    if song["genre"].lower() == favorite_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == favorite_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_difference = abs(song["energy"] - target_energy)
    energy_points = max(0.0, 2.0 * (1.0 - energy_difference))

    score += energy_points
    reasons.append(
        f"energy similarity (+{energy_points:.2f})"
    )

    if "valence" in user_prefs:
        target_valence = float(user_prefs["valence"])
        valence_difference = abs(song["valence"] - target_valence)
        valence_points = max(0.0, 1.0 - valence_difference)

        score += valence_points
        reasons.append(
            f"valence similarity (+{valence_points:.2f})"
        )

    if "danceability" in user_prefs:
        target_danceability = float(user_prefs["danceability"])
        danceability_difference = abs(
            song["danceability"] - target_danceability
        )
        danceability_points = max(
            0.0,
            1.0 - danceability_difference,
        )

        score += danceability_points
        reasons.append(
            f"danceability similarity (+{danceability_points:.2f})"
        )

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top-k recommendations."""

    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)

        scored_songs.append(
            (song, score, explanation)
        )

    ranked_songs = sorted(
        scored_songs,
        key=lambda result: result[1],
        reverse=True,
    )

    return ranked_songs[:k] 


