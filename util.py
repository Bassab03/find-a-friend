from unidecode import unidecode

def interests(s):
    """Parses a list of interests or subreddits. The input is case insensitive
    and supported delimiters are `,` and `and`.
    """
    return [unidecode(i.strip()) for i in s.lower().replace("and", ",").split(",") if i]

def username(u):
    """Parses a Reddit username. The input is case insensitive and is allowed to
    be prefixed with `u/` or `/u/`. Whitespace will be removed.
    """
    return u.replace(" ", "").lower().split("u/")[-1]