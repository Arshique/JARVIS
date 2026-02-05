import subprocess
from utils.config_loader import load_config

APP_INDEX = load_config("config/app_index.json")

def open_application(app):
    if app in APP_INDEX:
        subprocess.Popen([APP_INDEX[app]])
        return f"Opening {app.title()}"
    return "Application not found"

