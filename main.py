# This script reads from a file `input.csv` that has been *directly* exported
# from our spreadsheet in CSV format. It outputs a CSV-formatted list of paired
# users to standard output.

import csv
import operator
import scoreboard
from unidecode import unidecode

def interests(s):
    return [unidecode(i.strip()) for i in s.lower().replace("and", ",").split(",") if i]

def username(u):
    return u.replace(" ", "").lower().split("u/")[-1]

with open("input.csv", newline="") as csvfile:
    users = {}
    for row in csv.reader(csvfile):
        # Only parse the row if that user hasn't already been matched.
        if not row[2]:
            users[username(row[1])] = {
                "age": row[3],
                "gender": row[7],
                "interests": interests(row[4]),
                "meme_subreddits": interests(row[8]),
                "subreddits": interests(row[5]),
                "target_gender": row[6],
            }

    matches = []
    items = list(users.items())
    for i, (name1, user1) in enumerate(items):
        for name2, user2 in items[(i + 1):]:
            # Calculate the match score of the two users.
            score = scoreboard.category("interests", user1, user2)
            score += scoreboard.category("subreddits", user1, user2)
            score *= scoreboard.age(user1, user2)
            score *= scoreboard.gender(user1, user2)
            score *= scoreboard.memes(user1, user2)
            if score > 0:
                matches.append((score, name1, name2))

    # Move the highest scoring matches to the front of the list.
    matches.sort(key=operator.itemgetter(0), reverse=True)
    for (score, name1, name2) in matches:
        if name1 in users and name2 in users:
            print(f"{name1},{name2}")
            del users[name1]
            del users[name2]
