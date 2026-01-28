import subprocess
from config.settings import APP_PATHS, WEBSITES

def open_website(site):
    chrome_path = APP_PATHS["chrome"]
    url = WEBSITES[site]
    subprocess.Popen([chrome_path, url])
    return f"Opening {site.title()}"
