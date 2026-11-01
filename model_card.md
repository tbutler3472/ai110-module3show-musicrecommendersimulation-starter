# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
MusicMatch 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 


MusicMatch 1.0 is a music recommendation system designed to recommend songs based on a user's preferences for genre, mood, energy, and valence. The system assumes that users know what type of music they prefer and can provide those preferences to receive recommendations. This project is mainly designed for classroom exploration to demonstrate how recommendation systems use different features to rank songs.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  


My system works by comparing what the user likes with the songs in the dataset. It looks at things like genre, mood, energy, and valence to figure out which songs would be the best match. Genre and mood are worth 30% each, while energy and valence are worth 20% each. Based on this, each song gets a score, and the ones with the highest scores are recommended first. I also made changes to the starter code so it could read the songs from the dataset, score them, and give reasons for why they were recommended.

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  


My dataset has 20 songs with different genres like pop, rock, hip-hop, and lofi, along with moods like happy, chill, and intense. I added 10 more songs to the original dataset so the system would have more songs to choose from. Even though I added more songs, the dataset is still pretty limited since it doesn't have every genre or mood, so it may not match everyone's music preferences.

---

## 5. Strengths  

Where does your system seem to work well  


One strength of my recommendation system is that it does a good job finding songs that match what the user is looking for. When I tested the three different profiles, the top songs matched the genres and moods I expected. The system also looks at energy and valence instead of just genre, which helps it recommend songs based on more than one preference.  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

One limitation of my recommendation system is that it doesn't consider other features like tempo, danceability, or acousticness when recommending songs. Another limitation is that the dataset only has 20 songs, so certain genres and moods have more options than others. The system can also focus too much on one preference, like genre or mood, which could cause some songs to rank higher even if they don't match the user's other preferences. This could also make the recommendations less accurate for users who care more about energy or other features since the scoring weights are the same for everyone. One way I could improve my recommendation system would be to add more songs to the dataset and allow users to adjust the scoring weights based on which features matter most to them.

---

## 7. Evaluation  

## Evaluation

To evaluate my recommendation system, I tested three different user profiles: High-Energy Pop, Chill Lofi, and Intense Rock. Each profile had different preferences for genre, mood, energy, and valence.

I looked at the top five recommendations for each profile to see if the songs matched the user's preferences and if the scores made sense. The top recommendations matched what I expected based on the scoring system.

One thing that surprised me was Gym Hero appearing in both the High-Energy Pop and Intense Rock recommendations. This happened because the song matched different features for each profile.

I also tested changing the scoring weights by lowering the genre weight and increasing the energy weight. The top songs stayed the same, but some of the other songs changed positions. This showed how changing the weights can affect the recommendations.  

High-Energy Pop and Chill Lofi had different recommendations because one focused on upbeat songs while the other preferred calmer songs. High-Energy Pop and Intense Rock both preferred higher-energy songs, which explains why Gym Hero appeared in both. Lastly, Chill Lofi and Intense Rock had different results because of their differences in energy, mood, and genre.

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  


One thing I would want to improve is adding more songs to the dataset and using other features like tempo and danceability. I would also want users to be able to change the scoring weights based on what they care about more when listening to music. Another thing I could improve is giving users more variety in their recommendations and better explanations for why certain songs were chosen.

---

## 9. Personal Reflection  

A few sentences about your experience.  


In this project, I learned how recommendation systems use different features to figure out what songs a user might like. One thing I found interesting was how changing the scoring weights caused some songs to rank higher than others. I also learned how the dataset can affect the recommendations since there are only so many songs to choose from. This helped me understand more about how music recommendation apps work and why they recommend certain songs. 

### Stress Test Results

The recommendation system was tested using three different user profiles to see how the recommendations changed based on genre, mood, energy, and valence.

#### High-Energy Pop

```text
Preferences: genre=pop, mood=happy, energy=0.90, valence=0.85

Top 5 recommendations:

1. Sunrise City by Neon Echo
   Score: 98.20 / 100
   Reasons:
   - genre match (+30.00 points)
   - mood match (+30.00 points)
   - energy similarity (+18.40 points)
   - valence similarity (+19.80 points)

2. Saturday Starlight by Golden Hour Club
   Score: 68.60 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood match (+30.00 points)
   - energy similarity (+19.40 points)
   - valence similarity (+19.20 points)

3. Gym Hero by Max Pulse
   Score: 67.80 / 100
   Reasons:
   - genre match (+30.00 points)
   - mood mismatch (+0.00 points)
   - energy similarity (+19.40 points)
   - valence similarity (+18.40 points)

4. Rooftop Lights by Indigo Parade
   Score: 66.40 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood match (+30.00 points)
   - energy similarity (+17.20 points)
   - valence similarity (+19.20 points)

5. City Cypher by Northside Verse
   Score: 36.20 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood mismatch (+0.00 points)
   - energy similarity (+18.80 points)
   - valence similarity (+17.40 points)
```

#### Chill Lofi

```text
Preferences: genre=lofi, mood=chill, energy=0.35, valence=0.55

Top 5 recommendations:

1. Library Rain by Paper Lanterns
   Score: 99.00 / 100
   Reasons:
   - genre match (+30.00 points)
   - mood match (+30.00 points)
   - energy similarity (+20.00 points)
   - valence similarity (+19.00 points)

2. Midnight Coding by LoRoom
   Score: 98.40 / 100
   Reasons:
   - genre match (+30.00 points)
   - mood match (+30.00 points)
   - energy similarity (+18.60 points)
   - valence similarity (+19.80 points)

3. Focus Flow by LoRoom
   Score: 68.20 / 100
   Reasons:
   - genre match (+30.00 points)
   - mood mismatch (+0.00 points)
   - energy similarity (+19.00 points)
   - valence similarity (+19.20 points)

4. Spacewalk Thoughts by Orbit Bloom
   Score: 66.60 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood match (+30.00 points)
   - energy similarity (+18.60 points)
   - valence similarity (+18.00 points)

5. Quiet Constellation by Elian Wren
   Score: 38.60 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood mismatch (+0.00 points)
   - energy similarity (+19.20 points)
   - valence similarity (+19.40 points)
```

#### Intense Rock

```text
Preferences: genre=rock, mood=intense, energy=0.95, valence=0.40

Top 5 recommendations:

1. Storm Runner by Voltline
   Score: 97.60 / 100
   Reasons:
   - genre match (+30.00 points)
   - mood match (+30.00 points)
   - energy similarity (+19.20 points)
   - valence similarity (+18.40 points)

2. Gym Hero by Max Pulse
   Score: 62.20 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood match (+30.00 points)
   - energy similarity (+19.60 points)
   - valence similarity (+12.60 points)

3. Neon Overdrive by Prism Circuit
   Score: 34.80 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood mismatch (+0.00 points)
   - energy similarity (+20.00 points)
   - valence similarity (+14.80 points)

4. Night Drive Loop by Neon Echo
   Score: 34.20 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood mismatch (+0.00 points)
   - energy similarity (+16.00 points)
   - valence similarity (+18.20 points)

5. Last Train North by The Low Signals
   Score: 33.20 / 100
   Reasons:
   - genre mismatch (+0.00 points)
   - mood mismatch (+0.00 points)
   - energy similarity (+13.60 points)
   - valence similarity (+19.60 points)
```