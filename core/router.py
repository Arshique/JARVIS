from skills.open_app import open_application
from skills.open_website import open_website
from skills.close_app import close_application
from skills.search_web import search
from skills.system_info import get_time
from core.response import format_response
from skills.study_mode import start_study
from config.settings import WEBSITES
from utils.fuzzy_matcher import fuzzy_match
import json

with open("config/app_index.json") as f:
    APP_INDEX = json.load(f)

def route_command(data):
    intent = data["intent"]
    entity = data["entity"]

    if intent == "open_app":
        # combine all possible targets
        possible_targets = list(APP_INDEX.keys()) + list(WEBSITES.keys())
        entity = fuzzy_match(entity, possible_targets)

        if entity in WEBSITES:
            return open_website(entity)
        return open_application(entity)

    if intent == "close_app":
        entity = fuzzy_match(entity, list(APP_INDEX.keys()))
        return close_application(entity)

    if intent == "search_web":
        return search(data["raw"])

    if intent == "get_time":
        return get_time()

    if intent == "study_mode":
        return start_study()

    result = "Sorry, I don't understand that yet."
    return format_response(result)


