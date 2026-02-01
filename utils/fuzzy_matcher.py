from difflib import get_close_matches

def fuzzy_match(query, choices, cutoff=0.6):
    """
    Returns the closest match from choices for the given query.
    If no good match is found, returns the original query.
    """
    matches = get_close_matches(query, choices, n=1, cutoff=cutoff)
    return matches[0] if matches else query
