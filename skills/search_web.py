import webbrowser

def search(text):
    query = text.replace("search", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching for {query}"
