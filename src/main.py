"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def print_results_table(recommendations, user_prefs):
    """Prints a formatted ASCII table of the top recommendations."""
    col_rank   = 4
    col_title  = 26
    col_score  = 10
    col_reason = 34
    total_width = col_rank + col_title + col_score + col_reason + 7

    divider   = "+" + "-" * col_rank + "+" + "-" * col_title + "+" + "-" * col_score + "+" + "-" * col_reason + "+"
    header_ln = "+" + "=" * col_rank + "+" + "=" * col_title + "+" + "=" * col_score + "+" + "=" * col_reason + "+"

    print()
    print("=" * total_width)
    label = f"  Top {len(recommendations)} Recommendations  |  genre={user_prefs['genre']}  mood={user_prefs['mood']}  energy={user_prefs['energy']}"
    print(label)
    print("=" * total_width)

    def row(rank, title, score, reason):
        r = str(rank).center(col_rank) if rank else " " * col_rank
        t = title[:col_title - 1].ljust(col_title - 1) + " "
        s = score.center(col_score) if score else " " * col_score
        rs = reason[:col_reason - 1].ljust(col_reason - 1) + " "
        return f"|{r}|{t}|{s}|{rs}|"

    print(row(" # ", " Song", " Score", " Why"))
    print(header_ln)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        reasons = explanation.split(" | ")
        title_line  = song['title']
        artist_line = f"by {song['artist']}"

        print(row(i, title_line, f"{score:.2f}/5.00", reasons[0]))
        print(row("", artist_line, "", reasons[1] if len(reasons) > 1 else ""))
        for reason in reasons[2:]:
            print(row("", "", "", reason))
        print(divider)

    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Taste profile: late-night study session listener
    user_prefs = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.40,
        "likes_acoustic": True,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_results_table(recommendations, user_prefs)


if __name__ == "__main__":
    main()
