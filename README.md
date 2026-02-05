# 🤖 JARVIS – Personal Desktop Assistant (v0.3)

JARVIS is a Python-based personal desktop assistant designed to automate everyday desktop tasks using natural language commands.  
This version improves usability by handling imperfect user input safely and intelligently.

---

## 🚀 Features

- Open and close desktop applications
- Open websites in browser
- Search the web using commands
- Command normalization (handles natural sentences)
- Fuzzy command matching (handles typos)
- Confidence-based confirmation for uncertain actions
- Multiple exit keywords support (exit, bye, quit, etc.)
- Basic study mode automation
- Get current system time
- One-time automatic application scanning (Windows)

---

## 🧠 Architecture Overview

JARVIS follows a layered, rule-based architecture:

User Input  
→ Command Normalization  
→ Intent Detection  
→ Entity Extraction  
→ Fuzzy Matching & Validation  
→ Command Routing  
→ Skill Execution  

Each layer has a single responsibility, making the system modular and easy to extend.

---

## 📂 Project Structure

```text
jarvis/
├── core/
│   ├── brain.py
│   ├── router.py
│   ├── normalizer.py
│   ├── session.py
│   └── response.py
│
├── skills/
│   ├── open_app.py
│   ├── close_app.py
│   ├── open_website.py
│   ├── search_web.py
│   ├── study_mode.py
│   └── system_info.py
│
├── utils/
│   └── fuzzy_matcher.py
│
├── tools/
│   └── app_scanner.py
│
├── config/
│   └── settings.py
│
├── main.py
├── LICENSE
└── README.md
```

---

## 🛠 Tech Stack

- Python 3.10+
- subprocess
- webbrowser
- datetime
- difflib
- pylnk3

---

## ▶️ Running the Project

Run the application scanner once to index installed apps:
- python tools/app_scanner.py

Start JARVIS:
- python main.py

Exit JARVIS using:
- exit / quit / bye / shutdown......

------


## 🔐 Privacy & Security

- Application paths are generated locally
- App index file is excluded via .gitignore
- No user data is collected or transmitted
- No external APIs are used

---

## ⚠️ Limitations (v0.3)

- Text-based input only
- Rule-based intent detection
- No voice support
- No AI fallback

---

## 🛣 Roadmap

- Task-based shortcuts
- Logging system
- Voice input
- Optional AI-based fallback

---

# Changelog

## v0.1
- Initial rule-based desktop assistant
- App and website control

## v0.2
- Added fuzzy command matching for apps and websites

## v0.3
- Added command normalization
- Added confidence-based confirmation
- Improved exit command handling

---

## 📌 Project Status

Version: v0.3   
Platform: Windows  
Development Stage: Active development

---

## 📄 License

This project is intended for educational and personal use.
