# 🎵 Music Recommender Simulation

## Project Summary

This project implements a content-based music recommendation system in Python. It loads song information from a CSV file, compares each song to a user's music preferences, calculates a weighted recommendation score, and returns the highest ranked songs with explanations describing why they were recommended.


## How The System Works

The recommender uses content-based filtering. Every song contains descriptive features such as genre, mood, energy, valence, danceability, and acousticness.

A user profile stores preferred values for those same features.

Each song is compared against the user's preferences.

Scoring rules:

- Genre match = +2 points
- Mood match = +1 point
- Energy similarity = up to +2 points
- Valence similarity = up to +1 point
- Danceability similarity = up to +1 point

After every song is scored, the songs are sorted from highest score to lowest score. The five highest scoring songs are returned as recommendations along with an explanation describing why they matched the user's preferences.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```text
Loaded songs: 10

Top recommendations:

1. Sunrise City
Score: 6.89

2. Gym Hero
Score: 5.53

3. Rooftop Lights
Score: 4.81

4. Night Drive Loop
Score: 3.42

5. Storm Runner
Score: 3.38
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

- Increased the weight for genre matching to improve recommendations for users who strongly prefer one music genre.
- Adjusted the energy similarity calculation to better rank songs with similar energy levels.
- Added valence and danceability similarity so recommendations consider more than just genre and mood. 

## Limitations and Risks

This recommender has several limitations.

- It only works with a very small music catalog.
- It cannot understand lyrics or song meaning.
- It does not learn from previous recommendations.
- Recommendations depend entirely on manually selected song features.
- Different users may value music characteristics differently, but every user is scored using the same weighting system.
---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

Building this recommender helped me understand how recommendation systems compare user preferences with item features to generate personalized suggestions. I learned how weighted scoring can significantly affect the ranking of recommendations.

I also learned that recommendation systems can introduce bias depending on which features receive the highest weights. Future improvements could include collaborative filtering, user feedback, and machine learning models that automatically learn feature importance from user behavior.





