from core.router import route_command

def process_input(text):
    intent_data = understand(text)
    return route_command(intent_data)

def understand(text):
    return {
        "raw": text,
        "intent": detect_intent(text),
        "entity": detect_entity(text)
    }

def detect_intent(text):
    if "study" in text:
        return "study_mode"
    if "open" in text:
        return "open_app"
    if "search" in text:
        return "search_web"
    if "time" in text:
        return "get_time"
    return "unknown"


def detect_entity(text):
    words = text.split()
    if "counter strike" in text or "csgo" in words:
        return "counter strike"
    if "chrome" in words:
        return "chrome"
    if "youtube" in words:
        return "youtube"
    if "google" in words:
        return "google"
    if "gmail" in words:
        return "gmail"
    if "github" in words:
        return "github"
    return None
