import subprocess

def running_app():
    result = subprocess.run(['tasklist'], capture_output = True, text = True )
    
    lines = result.stdout.splitlines()

    running_apps = []

    for line in lines[3:]:

        parts = line.split()
        if not parts:
            continue
        process_name = parts[0].lower()
        running_apps.append(process_name)

    return running_apps