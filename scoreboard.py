GENDER_FACTOR = 1
MEME_FACTOR = 0.25

def age(user1, user2):
    diff = abs(age_to_number(user1["age"]) - age_to_number(user2["age"]))
    return 1 / (1 + diff / 3)

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

def category(category, user1, user2):
    i = 0
    for j in user1[category]:
        i += user2[category].count(j)
    return i

def gender(user1, user2):
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

def memes(user1, user2):
    one = user1["meme_subreddits"]
    two = user2["meme_subreddits"]
    is_match = not one or not two or not set(one).isdisjoint(two)
    return 1 + MEME_FACTOR * int(is_match)