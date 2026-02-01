from core.normalizer import normalize_command
from core.router import route_command
import core.session as session


def process_input(text):
    text = text.lower().strip()

    # Handle confirmation replies
    if session.pending_confirmation:
        if text in {"yes", "y"}:
            data = session.pending_confirmation
            session.pending_confirmation = None
            return route_command(data)

        if text in {"no", "n"}:
            session.pending_confirmation = None
            return "Okay, cancelled."

        return "Please reply with yes or no."

    normalized_text = normalize_command(text)
    intent_data = understand(normalized_text)
    return route_command(intent_data)


def understand(text):
    return {
        "raw": text,
        "intent": detect_intent(text),
        "entity": detect_entity(text)
    }


def detect_intent(text):
    words = text.split()

    if "study" in words:
        return "study_mode"
    if "open" in words:
        return "open_app"
    if "close" in words:
        return "close_app"
    if "search" in words:
        return "search_web"
    if "time" in words:
        return "get_time"

    return "unknown"


def detect_entity(text):
    remove_words = {
        "open", "close", "search", "study",
        "please", "jarvis", "hey"
    }

    words = text.split()
    entity_words = [w for w in words if w not in remove_words]

    return " ".join(entity_words)
