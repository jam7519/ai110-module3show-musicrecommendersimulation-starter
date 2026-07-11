"""
Command-line runner for the Music Recommender Simulation.

Run from the project root with:

    python -m src.main
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    """Load songs, build a sample user profile, and print recommendations."""

    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "valence": 0.9,
        "danceability": 0.8,
    }

    recommendations = recommend_songs(
        user_prefs=user_prefs,
        songs=songs,
        k=5,
    )

    print("\nUser profile:")
    print(
        f"Genre: {user_prefs['genre']}, "
        f"Mood: {user_prefs['mood']}, "
        f"Energy: {user_prefs['energy']}"
    )

    print("\nTop recommendations:")

    for position, (song, score, explanation) in enumerate(
        recommendations,
        start=1,
    ):
        print(
            f"\n{position}. {song['title']} by {song['artist']}"
        )
        print(
            f"   Genre: {song['genre']} | "
            f"Mood: {song['mood']} | "
            f"Energy: {song['energy']:.2f}"
        )
        print(f"   Score: {score:.2f}")
        print(f"   Because: {explanation}")


if __name__ == "__main__":
    main()


    