from skills.open_app import open_application
from skills.open_website import open_website
from skills.close_app import close_application
from skills.search_web import search
from skills.system_info import get_time
from core.response import format_response
from skills.study_mode import start_study
from config.settings import WEBSITES
from utils.fuzzy_matcher import fuzzy_match_with_confidence
from utils.config_loader import load_config
import core.session as session

APP_INDEX = load_config("config/app_index.json")

def route_command(data):
    global pending_confirmation

    intent = data["intent"]
    entity = data["entity"]

    if intent == "open_app":
        targets = list(APP_INDEX.keys()) + list(WEBSITES.keys())
        match, confidence = fuzzy_match_with_confidence(entity, targets)

        # No match at all
        if not match:
            return "Application or website not found."

        # Low confidence → ask confirmation
        if confidence < 0.75:
            session.pending_confirmation = {
                "intent": "open_app",
                "entity": match
            }
            return f"Did you mean '{match}'? (yes/no)"

        # High confidence → execute
        if match in WEBSITES:
            return open_website(match)

        return open_application(match)

    if intent == "close_app":
        match, confidence = fuzzy_match_with_confidence(entity, list(APP_INDEX.keys()))

        if confidence < 0.75:
            session.pending_confirmation = {
                "intent": "close_app",
                "entity": match
            }
            return f"Did you mean '{match}'? (yes/no)"

        if match:
            return close_application(match)

        return "Application not found."

    if intent == "search_web":
        return search(data["raw"])

    if intent == "get_time":
        return get_time()

    if intent == "study_mode":
        return start_study()

    if intent == "task_shortcut":
        # Placeholder for future task shortcut handling
        return


    if intent == "close_all_app":
        from skills.Close_all_app import close_all_app
        return close_all_app()
    return "Command not supported yet."
