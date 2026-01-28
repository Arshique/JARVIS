import subprocess
import json

with open("config/app_index.json") as f:
    APP_INDEX = json.load(f)

def open_application(app):
    if app in APP_INDEX:
        subprocess.Popen(APP_INDEX[app])
        return f"Opening {app.title()}"
    return "Application not found"

