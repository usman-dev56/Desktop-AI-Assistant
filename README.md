# 🤖 AI Desktop Assistant

A modern desktop voice assistant built with **Python** that can control applications, websites, windows, and media using natural voice commands.



---

##  Features

### 🎙 Voice Interaction

* Wake word detection
* Speech-to-Text (Voice Recognition)
* Text-to-Speech (Edge-TTS)
* Natural command normalization

### 🖥 Desktop Automation

* Open desktop applications
* Close desktop applications
* Focus application windows
* Minimize windows
* Maximize windows
* Restore minimized windows

### 🌐 Browser Control

* Open websites
* Default browser support

### 🎵 Media

* Play music from YouTube
* Favorite songs support
* Automatic YouTube search for unknown songs

### 📷 Screenshot

* Capture full-screen screenshots
* Automatically save screenshots with timestamps

### 🛠 Utilities

* Current time
* Current date
* Exit assistant

---

# 📁 Project Structure

```text
AI-Desktop-Assistant/
│
├── app/
│   ├── assistant/
│   ├── commands/
│   ├── services/
│   ├── speech/
│   ├── core/
│   ├── utils/
│   ├── models/
│   └── config.py
│
├── assets/
├── screenshots/
├── logs/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# 🚀 Technologies Used

* Python 3.12+
* SpeechRecognition
* Edge-TTS
* pygame
* pywhatkit
* pyautogui
* pygetwindow
* psutil
* python-dotenv

---

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/usman-dev56/AI-Desktop-Assistant.git
```

Move into the project

```bash
cd AI-Desktop-Assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the assistant

```bash
python -m app.main
```

---

# 🎤 Example Commands

## Desktop

* Open Chrome
* Open Calculator
* Open Notepad
* Close Chrome
* Close Notepad

## Window Management

* Focus Chrome
* Minimize Chrome
* Maximize Chrome
* Restore Chrome

## Browser

* Open Google
* Open YouTube
* Open GitHub

## Music

* Play Believer
* Play Faded
* Play Relaxing Music
* Play Quran
* Play Study Music

## Screenshot

* Screenshot
* Take Screenshot
* Capture Screen

## Utility

* What time is it?
* What is today's date?
* Exit
* Close

---

# 🏗 Current Architecture

```text
Assistant
    │
    ▼
Command Processor
    │
    ▼
Command Router
    │
    ├── Browser Service
    ├── Desktop Service
    ├── Music Service
    ├── Window Service
    ├── Screenshot Service
    ├── Time Service
    └── Date Service
```


# 🤝 Contributing

Contributions, ideas, and feature suggestions are welcome.

Feel free to fork the repository, create a feature branch, and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Usman**

* GitHub: https://github.com/usman-dev56

---

⭐ If you like this project, consider giving it a star!
