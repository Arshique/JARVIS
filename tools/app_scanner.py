import os
import json
import pylnk3

START_MENU_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs")
]

apps = {}

for base_path in START_MENU_PATHS:
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".lnk"):
                shortcut_path = os.path.join(root, file)
                try:
                    with open(shortcut_path, "rb") as f:
                        lnk = pylnk3.parse(f)
                        target = lnk.path

                        if target and os.path.exists(target):
                            app_name = file.replace(".lnk", "").lower()
                            apps[app_name] = target
                except:
                    pass

# Save app index
with open("config/app_index.json", "w") as f:
    json.dump(apps, f, indent=4)

print(f"✅ App scan complete. {len(apps)} apps indexed.")