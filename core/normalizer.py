def normalize_command(text):
    text = text.lower().strip()

    # words to remove (noise)
    noise_words = {
        "hey", "hi", "hello", "jarvis", "please",
        "can", "you", "could", "would", "for", "me",
        "the", "a", "an", "to", "up", "now"
    }

    words = text.split()
    cleaned_words = [word for word in words if word not in noise_words]

    return " ".join(cleaned_words)
