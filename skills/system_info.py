import datetime

def get_time():
    now = datetime.datetime.now()
    return f"The time is {now.strftime('%H:%M')}"
