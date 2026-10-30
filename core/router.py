from skills.open_app import open_application
from skills.open_website import open_website
from skills.close_app import close_application
from skills.search_web import search
from skills.system_info import get_time
from skills.study_mode import start_study
from config.settings import WEBSITES
from utils.fuzzy_matcher import fuzzy_match_with_confidence
from utils.config_loader import load_config
import core.session as session

APP_INDEX = load_config("config/app_index.json")

def route_command(data):

    intent = data["intent"]
    
    handler = INTENT_HANDLERS.get(intent)

    if handler:
        return handler(data)

    return "Command not supported yet."


def handle_open_app(data):
    entity = data["entity"]

    if data.get("confirmed"):
        if entity in WEBSITES:
            return open_website(entity)
        
        return open_application(entity)

    targets = list(APP_INDEX.keys()) + list(WEBSITES.keys())
    match, confidence = fuzzy_match_with_confidence(entity, targets)

    if not match:
        return "Application or website not found."

    if confidence < 0.75:
        session.pending_confirmation = {
            "intent": "open_app",
            "entity": match
        }
        return f"Did you mean '{match}'? (yes/no)"

    if match in WEBSITES:
        return open_website(match)

    return open_application(match)

def handle_close_app(data):

    entity = data["entity"]

    if data.get("confirmed"):
        return close_application(entity)

    match, confidence = fuzzy_match_with_confidence(entity, list(APP_INDEX.keys()))
    if confidence < 0.75:
        session.pending_confirmation = {
            "intent": "close_app",
            "entity": match
        }
        return f"Did you mean '{match}'? (yes/no)"

    if match:
        return close_application(match)
    else:
        return "Application not found!"
    
def handle_search_web(data):
    return search(data["raw"])

def handle_get_time(data):
    return get_time()


def handle_study_mode(data):
    return start_study()


def handle_task_shortcut(data):
    # Placeholder for future task shortcut handling
    return "Task shortcuts are not implemented yet."


def handle_close_all_app(data):
    from skills.remove_distraction import close_all_app
    return close_all_app()
    

INTENT_HANDLERS = {
    "open_app": handle_open_app,
    "close_app": handle_close_app,
    "search_web": handle_search_web,
    "get_time": handle_get_time,
    "study_mode": handle_study_mode,
    "task_shortcut": handle_task_shortcut,
    "close_all_app": handle_close_all_app,
}
