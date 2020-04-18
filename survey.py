import csv
import operator
import random
from unidecode import unidecode

GENDER_FACTOR = 1
MEME_FACTOR = 0.25


def age_to_number(age):
    if age == "12 or less":
        return 12
    elif age == "18 - 19":
        return 18.5
    elif age == "20+":
        return 20
    elif not age:
        return 16
    else:
        return int(age)

def age_interest(user1, user2):
    diff = abs(age_to_number(user1["age"]) - age_to_number(user2["age"]))
    return 1 / (1 + diff / 3)

def cat_score(category, user1, user2):
    i = 0
    for j in user1[category]:
        i += user2[category].count(j)
    return i


def gender_interest(user1, user2):
    match1 = is_gender_match(user2["gender"], user1["target_gender"])
    match2 = is_gender_match(user1["gender"], user2["target_gender"])
    return 1 + 0.5 * GENDER_FACTOR * (int(match1) + int(match2))

def is_gender_match(gender, target_gender):
    if not gender or not target_gender or target_gender == "Doesn't matter":
        return True
    elif gender == "Female" and target_gender == "Girl":
        return True
    elif gender == "Male" and target_gender == "Boy":
        return True
    elif gender == "Non-binary / other" and target_gender == "Non-binary / other":
        return True
    else:
        return False


def is_meme_match(one, two):
    return not one or not two or one == two

def meme_interest(user1, user2):
    one = user1["meme_subreddit"]
    two = user2["meme_subreddit"]
    return 1 + MEME_FACTOR * int(is_meme_match(one, two))


def parse_list(s):
    return [unidecode(i.strip()) for i in s.lower().replace("and", ",").split(",") if i]


with open("input.csv", newline="") as csvfile:
    users = {}

    rows = list(csv.reader(csvfile))
    for row in rows:
        if not row[2]:
            users[row[1]] = {
                "age": row[3],
                "gender": row[7],
                "interests": parse_list(row[4]),
                "meme_subreddit": parse_list(row[8]),
                "subreddits": parse_list(row[5]),
                "target_gender": row[6],
                "username": row[1],
            }

    matches = []
    items = list(users.items())
    for i, (name1, user1) in enumerate(items):
        for (name2, user2) in items[(i + 1):]:
            if name1 in users and name2 in users:
                score = cat_score("interests", user1, user2)
                score += cat_score("subreddits", user1, user2)
                score *= age_interest(user1, user2)
                score *= gender_interest(user1, user2)
                score *= meme_interest(user1, user2)
                if score > 0:
                    matches.append((score, name1, name2))

    matches.sort(key=operator.itemgetter(0), reverse=True)
    for (score, name1, name2) in matches:
        if name1 in users and name2 in users:
            print(name1, name2)
            del users[name1]
            del users[name2]
