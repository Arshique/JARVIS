from difflib import SequenceMatcher, get_close_matches

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def fuzzy_match_with_confidence(query, choices):
    if not query:
        return None, 0.0

    matches = get_close_matches(query, choices, n=1, cutoff=0.4)

    if not matches:
        return None, 0.0

    best_match = matches[0]
    confidence = similarity(query, best_match)
    return best_match, confidence
