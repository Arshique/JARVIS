import subprocess
import json
import os

# load app index
with open("config/app_index.json") as f:
    APP_INDEX = json.load(f)

# websites live inside chrome
WEBSITE_ALIASES = {"youtube", "google", "gmail", "github"}

def close_application(app):
    # if user says "close youtube", close chrome
    if app in WEBSITE_ALIASES:
        app = "chrome"

    if app not in APP_INDEX:
        return "Application not found"

    exe_path = APP_INDEX[app]

    # extract process name from exe path
    process_name = os.path.basename(exe_path)

    subprocess.run(
        ["taskkill", "/f", "/im", process_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return f"Closed {app.title()}"
