# import os
import subprocess
from config.settings import APP_PATHS, WEBSITES

def open_application(app):
    if app in APP_PATHS:
        subprocess.Popen(APP_PATHS[app])
        return f"Opening {app.title()}"
    return "Application not found"
