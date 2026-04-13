# Reflection: Profile Comparisons

---

## High-Energy Pop vs Chill Lofi

These two profiles are basically opposites and the system handled the difference well. The pop profile wanted loud, fast, happy music with no acoustic instruments. The lofi profile wanted quiet, slow, chill music with acoustic texture. The top results for each were completely different songs with almost no overlap. That makes sense because these listeners have nothing in common on any of the four scoring dimensions.

The interesting thing is that both profiles still struggled below the top two or three results. Once the system ran out of songs that genuinely matched, it started filling the list with songs that shared one or two numbers but had totally different vibes. The pop listener got metal songs in the bottom of the list. The lofi listener got jazz and ambient. Those are close-ish but not really the same thing.

---

## Chill Lofi vs Deep Intense Rock

This comparison shows the catalog problem most clearly. The lofi profile had three real matches (Midnight Coding, Library Rain, Focus Flow) before running out of good options. The rock profile had exactly one real match (Storm Runner) and then nothing. After Storm Runner everything below it was filler picked by energy level alone. Crown Moves (hip-hop) and Peak Hour (EDM) both ended up in the top five for a rock listener, which a real rock fan would find pretty confusing.

The reason Gym Hero kept showing up for the rock profile is that it is tagged "intense" like the user wanted, and its energy (0.93) is close to the target (0.90). So it picks up mood points and energy points even though it is a pop song. The system does not know that "intense pop" and "intense rock" feel like completely different things to a person. It just sees numbers and labels that partially match.

---

## Deep Intense Rock vs Edge: High Energy and Sad Mood (soul/sad at 0.90 energy)

This is the most useful comparison because it shows what happens when a user wants things that do not naturally go together. The rock profile worked pretty well because intense rock with high energy actually exists in the catalog. But the soul plus sad plus high energy profile did not work at all because that combination basically does not exist. Sad soul music is almost always low energy by nature.

The system did not flag this as a problem. It just picked the one soul song (Hollow Sunday), gave it a low score because the energy was wrong, and then filled the rest of the list with high-energy songs from completely different genres. From the outside the output looks like a normal recommendation list. But every result except number one is basically a guess. A real platform would either warn the user that their preferences conflict or ask a follow-up question to figure out which preference matters more.

---

## Edge: Blues with One Song vs Edge: EDM but Likes Acoustic

Both of these profiles exposed the same problem from two different angles. The blues profile got one perfect score (5.00 for Empty Bottle Blues) and then four songs that were just acoustically similar slow songs from other genres. The EDM profile got one partial match (Peak Hour scored 4.00 because it lost the acoustic point) and then four acoustic songs from genres like folk and country that have nothing to do with EDM.

In both cases the system filled empty slots with whatever scored highest on the numeric features, ignoring whether those songs made any real sense for the listener. The honest thing a system should probably do in these situations is return fewer results with a note saying the catalog does not have enough matches, rather than padding the list with songs that are technically close but practically wrong.
