# import os
import subprocess
from config.settings import APP_PATHS, WEBSITES

def open_application(app):
    if app == "chrome":
        subprocess.Popen(APP_PATHS[app])
        return
    if app in APP_PATHS:
        subprocess.Popen(APP_PATHS[app])
        return f"Opening {app.title()}"
    return "Application not found"
    
def open_website(site):
    chrome_path = APP_PATHS["chrome"]
    url = WEBSITES[site]

    subprocess.Popen([chrome_path, url])
    return f"Opening {site.title()}"