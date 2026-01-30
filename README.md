# 🤖 JARVIS – Personal Desktop Assistant (v0.1)

JARVIS is a Python-based personal desktop assistant designed to automate everyday desktop tasks using simple natural language commands. This version focuses on rule-based command execution and a modular system design.

---

## 🚀 Features (v0.1)

- Open and close desktop applications
- Open websites in browser
- Search the web using commands
- Basic study mode automation
- Get current system time
- One-time automatic application scanning (Windows)

---

## 🧠 Architecture Overview

JARVIS uses a modular, rule-based architecture:

User Input → Intent Detection → Entity Extraction → Command Routing → Skill Execution

Each component has a single responsibility, making the system easy to extend and maintain.

---

## 📂 Project Structure
```text
jarvis/                                                                                                                                                                        
├── core/
│ ├── brain.py
│ ├── router.py
│ └── response.py
│
├── skills/
│ ├── open_app.py
│ ├── close_app.py
│ ├── open_website.py
│ ├── search_web.py
│ ├── study_mode.py
│ └── system_info.py
│
├── tools/
│ └── app_scanner.py
│
├── config/
│ └── settings.py
│
├── main.py
└── README.md
```
---

## 🛠 Tech Stack

- Python 3.10+
- subprocess
- webbrowser
- datetime
- pylnk3

---

## ▶️ Running the Project

Run the application scanner once to index installed apps:
1. python tools/app_scanner.py
2. python main.py

------


## 🔐 Privacy & Security

- Application paths are generated locally
- App index file is excluded via .gitignore
- No user data is collected or transmitted
- No external APIs are used in v0.1

---

## ⚠️ Limitations (v0.1)

- Text-based input only
- Rule-based intent detection
- No fuzzy matching
- No voice support
- No AI fallback

---

## 🛣 Roadmap

- Fuzzy command matching
- Command normalization
- Enhanced study mode
- Task-based shortcuts
- Voice input
- Optional AI-based fallback

---

## 📌 Project Status

Version: v0.1  
Platform: Windows  
Development Stage: Early / Experimental

---

## 📄 License

This project is intended for educational and personal use.
