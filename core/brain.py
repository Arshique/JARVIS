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
    if "close" in text:
        return "close_app"
    if "search" in text:
        return "search_web"
    if "time" in text:
        return "get_time"
    return "unknown"


def detect_entity(text):
    return text.replace("open","").replace("close","").strip()