from skills.close_app import close_application
from skills.running_apps import running_app
from utils.config_loader import load_config
import os

protect_app = load_config("config/protected_apps.json")["protected_processes"]
app_index = load_config("config/app_index.json")

def close_all_app():
    running = running_app()

    exe_to_app = {os.path.basename(path).lower(): app for app, path in app_index.items()} 

    for process in running:
        process = process.lower()

        if process in protect_app:
            continue
        if process in exe_to_app:
            app_name = exe_to_app[process]
            close_application(app_name)     

    return "Focus Mode Activated"
    