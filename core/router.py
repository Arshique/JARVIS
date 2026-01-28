from skills.open_app import open_application
from skills.open_website import open_website
from skills.search_web import search
from skills.system_info import get_time
from core.response import format_response
from skills.study_mode import start_study
from config.settings import WEBSITES

def route_command(data):
    intent = data["intent"]
    entity = data["entity"]

    if intent == "open_app":
        if entity in WEBSITES:
            return open_website(entity)
        else:
            return open_application(entity)

    if intent == "search_web":
        return search(data["raw"])

    if intent == "get_time":
        return get_time()

    if intent == "study_mode":
        return start_study()

    result = "Sorry, I don't understand that yet."
    return format_response(result)

