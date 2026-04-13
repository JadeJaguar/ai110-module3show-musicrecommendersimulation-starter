# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This system is built for classroom exploration. It takes a user taste profile and suggests songs from a small catalog that match what the user says they want. It is designed to show how a basic content-based recommender works, not to serve real users on a real platform. It assumes the user already knows their preferred genre, mood, energy level, and whether they like acoustic or produced sound.

---

## 3. How the Model Works

Every song in the catalog gets a score based on how well it matches the user profile. Genre match is worth the most points because it is the strongest signal. Mood match is worth a bit less. Energy uses a sliding scale so songs that are closer to the user's preferred energy level score higher, not just the loudest or quietest ones. Acoustic preference is a simple yes or no check. The scores all add up and the top five songs win. No song is ever excluded entirely, it just scores lower if it does not match.

---

## 4. Data

The catalog has 20 songs stored in a CSV file. Each song has a title, artist, genre, mood, energy level, tempo, valence, danceability, and acousticness. The original starter file had 10 songs covering pop, lofi, rock, ambient, jazz, synthwave, and indie pop. We added 10 more to cover hip-hop, r&b, classical, metal, country, soul, edm, folk, latin, and blues. The catalog now has 17 genres and 16 moods. The big limit is that most genres only have one song, which means users who like underrepresented genres get thin results.

---

## 5. Strengths

The system works best when the user profile lines up with a well-represented genre. Lofi and pop listeners get the most genuine recommendations because those genres have two or three songs each. The scoring is fully transparent since every result comes with a plain-language explanation of exactly why it ranked where it did. The energy proximity formula works well for separating songs within the same genre, for example it correctly ranks Midnight Coding above Library Rain for a user who wants energy around 0.40 because Midnight Coding is slightly closer.

---

## 6. Limitations and Bias

The biggest weakness is that the catalog is not spread evenly across genres. Lofi and pop each have two or three songs, but genres like blues, metal, rock, and folk only have one song each. That means a blues listener gets one real recommendation and four filler songs that just happen to have similar energy levels. The system does not know the difference between a genuine match and a coincidental numeric match, so it serves those filler results with the same confidence as the real one. If this were a real product, users who like underrepresented genres would get a noticeably worse experience than users who like pop or lofi, which is a form of bias even if it was not intentional.

---

## 7. Evaluation

We tested six user profiles. Three were standard: High-Energy Pop, Chill Lofi, and Deep Intense Rock. Three were edge cases: a user with conflicting preferences (high energy but sad soul music), a user whose favorite genre only has one song in the catalog (blues), and a user who wants EDM but also likes acoustic sound.

The standard profiles mostly worked as expected. Chill Lofi and High-Energy Pop both surfaced the right songs at the top. The rock profile surprised us because after Storm Runner at number one, the next four results were hip-hop, EDM, and metal picked purely by energy level. A real rock fan would skip all of them.

The conflicting preferences profile was the most revealing. The system did not notice that high energy and sad soul music basically do not go together. It just kept scoring and returned high-energy songs from other genres as if that was a reasonable answer.

We also ran a weight shift experiment where we halved the genre points and doubled the energy points. The top results stayed the same but the scores below number one got much closer together, which showed that weakening genre lets wrong-genre songs creep toward the top.

---

## 8. Future Work

First, the catalog needs more songs per genre. Right now most genres have one song which makes the bottom of every recommendation list feel random. Adding five to ten songs per genre would make a noticeable difference in result quality.

Second, mood matching should give partial credit for similar moods. Right now chill and relaxed score zero against each other even though they feel almost identical. A simple lookup table of related moods would fix this.

Third, the system should detect when a user profile has conflicting preferences and either warn the user or ask which preference matters more before generating results.

---

## 9. Personal Reflection

The biggest learning moment was running the weight shift experiment. Halving the genre points and doubling the energy points kept the number one result the same but compressed all the scores below it until wrong-genre songs were nearly tied with correct ones. That one change made it really clear that the weights are not just decoration, they are the actual opinion the system has about what matters. Changing them changes the personality of the recommender completely.

Using AI tools helped a lot for getting started quickly and for thinking through edge cases that would have taken longer to spot manually. The adversarial profiles like the conflicting soul plus high energy user were suggested during the design phase and turned out to be the most useful tests. The one place where double checking mattered most was the scoring math. When the weight experiment ran, it was worth verifying by hand that the new max still added up to 5.0 before trusting the output, because a formula change that silently breaks the scale would make all the scores meaningless.

The most surprising thing was how much the results can feel right even though the system has no idea what music actually sounds like. It just knows that Midnight Coding has a number called energy equal to 0.42 and the user wants 0.40, so the gap is small. It does not know the song is calm and textured and good for studying. But because those attributes happen to be captured in the numbers, the recommendation lands correctly anyway. It feels intelligent but it is really just arithmetic on well-chosen features.

If this project continued the first thing to try would be partial mood matching using a small lookup table of related moods. Chill and relaxed scoring the same as chill and metal feels wrong and would be a quick fix with a noticeable improvement in result quality for a lot of user types.

---
