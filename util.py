from unidecode import unidecode

def interests(s):
    return [unidecode(i.strip()) for i in s.lower().replace("and", ",").split(",") if i]

def username(u):
    return u.replace(" ", "").lower().split("u/")[-1]