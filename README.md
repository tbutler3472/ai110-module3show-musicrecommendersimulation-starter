# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

How The System Works

Music recommendation systems use different approaches to predict what songs users may enjoy. Collaborative filtering focuses on what users with similar listening habits enjoy, while content-based filtering focuses on song attributes. My system will use content-based filtering to recommend songs based on the user's musical preferences.

Song Features

Each Song object will contain the song's ID, title, artist, genre, mood, energy, and valence. These attributes will help determine how closely a song matches the user's preferences.

UserProfile

The UserProfile will store the user's preferred genre, mood, energy, and valence. This information will be used to compare the user's preferences with the available songs.

Recommender

The Recommender will use a weighted scoring system to calculate how closely each song matches the user's preferences. Genre and mood will each account for 30% of the score, while energy and valence will each account for 20%. Energy and valence will be scored based on how close their values are to the user's preferences.

Choosing Recommendations

Once each song receives a score, the system will rank the songs from highest to lowest. The songs with the highest scores will be recommended first because they best match the user's musical preferences.
You can include a simple diagram or bullet list if helpful.

Algorithm Recipe

The recommendation system will use a weighted scoring algorithm to determine which songs best match the user's preferences. Genre and mood will each account for 30% of the score, while energy and valence will each account for 20%. Genre and mood will receive a score of 1 for a match and 0 for a mismatch. Energy and valence will be scored based on how close their values are to the user's preferences using the formula 1 - |Song Value - User Preference|. The system will then calculate a total score out of 100 for each song and rank them from highest to lowest to recommend the top matches.

Potential Biases

One potential bias in this system is that it may favor songs that match the user's preferred genre and mood while overlooking songs from other genres that the user might enjoy. Since the system relies on a limited dataset and specific song attributes, it may also recommend similar types of music repeatedly, limiting the variety of recommendations.
---


## Sample Recommendation Output

The following output shows the top five songs recommended by the system based on the default user preferences.

```text
Top recommendations:

1. Sunrise City by Neon Echo
   Score: 92.80 / 100
   Reasons:
   - genre match (+30.00 points)
   - mood match (+30.00 points)
   - energy similarity (+19.60 points)
   - valence similarity (+13.20 points)

2. Rooftop Lights by Indigo Parade
   Score: 63.00 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood match (+30.00 points)
   - energy similarity (+19.20 points)
   - valence similarity (+13.80 points)

3. Gym Hero by Max Pulse
   Score: 62.00 / 100
   Reasons:
   - genre match (+30.00 points)
   - mood mismatch (+0.00 points)
   - energy similarity (+17.40 points)
   - valence similarity (+14.60 points)

4. Saturday Starlight by Golden Hour Club
   Score: 60.80 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood match (+30.00 points)
   - energy similarity (+18.60 points)
   - valence similarity (+12.20 points)

5. Night Drive Loop by Neon Echo
   Score: 38.80 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood mismatch (+0.00 points)
   - energy similarity (+19.00 points)
   - valence similarity (+19.80 points)
```




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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



