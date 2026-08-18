
# 🤖 Jarvis — AI Desktop Voice Assistant

A modular Python-based desktop voice assistant that allows users to control desktop applications, manage windows, open websites, perform web searches, play music, take screenshots, and interact with their computer using voice commands.

> 🚀 This project is being developed as a learning and portfolio project and is currently being upgraded for the **Oasis Infobyte AICTE Internship — Python Programming Task 1**.

---

## ✨ Features

### 🎙️ Voice Interaction
- 🎤 Voice input through microphone
- 🗣️ Speech-to-text using `SpeechRecognition`
- 🔊 Text-to-speech using `Edge-TTS`
- 🧠 Command normalization
- 🔄 Natural command aliases
- 🎯 Wake-word handling
- 🧹 Filler-word removal
- ⚠️ Graceful speech recognition error handling

### 🖥️ Desktop Automation
- Open desktop applications
- Close desktop applications
- Focus application windows
- Minimize windows
- Maximize windows
- Restore windows
- Configurable application support

### 🌐 Browser Control
- Open websites using voice commands
- Default browser support
- Configurable website shortcuts

### 🔎 Web Search
Supports natural search commands such as:
- `Search Python FastAPI tutorials`
- `Google machine learning`
- `Look up REST APIs`
- `Find information about Python`

### 🎵 Music
- Play music through voice commands
- Favorite song shortcuts
- YouTube-based playback
- Support for unknown song searches

**Examples:**
```text
Play Believer
Play Faded
Play Relaxing Music
Play Study Music
```

### 📷 Screenshot
- Capture full screen
- Automatically save screenshots
- Timestamp-based screenshot filenames

### 🕐 Utilities
- Current time
- Current date
- Exit assistant

### 🌦️ Weather
- Weather service integrated using the OpenWeatherMap API.
- ⚠️ *Weather API integration is currently under testing because API authentication needs to be configured correctly.*


### ⏰ Timed Reminders
- Jarvis supports voice-controlled timed reminders.

**Examples:**
```text
Remind me in 10 seconds
Remind me in 10 seconds to drink water
Remind me in 2 minutes to check my work
```
---

## 🧠 Command Processing

Jarvis uses a modular command-processing architecture instead of putting all functionality inside one large file. Spoken commands are normalized before being passed to the command router.

For example:
```text
"Hey Jarvis, please launch Chrome"  ──▶  "open chrome"
"Jarvis, could you terminate Notepad" ──▶  "close notepad"
```

The parser currently supports:
- Wake-word removal
- Filler-word removal
- Command aliases
- Application aliases
- Alternative command phrases

---

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │    Microphone    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Listener     │
                    │ SpeechRecognition│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Command Parser  │
                    │   Normalization  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Command Router  │
                    └────────┬─────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
   │   Browser   │    │   Desktop   │    │    Music    │
   │   Commands  │    │   Commands  │    │   Commands  │
   └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
          │                  │                  │
          ▼                  ▼                  ▼
   BrowserService      DesktopService      MusicService
          │                  │                  │
          │                  ├── WindowService  │
          │                  │                  │
          └──────────────┬───┴──────────────────┘
                         │
                         ▼
                  Other Services
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
     TimeService    DateService   ScreenshotService
                         │
                         ▼
                  WeatherService
                         │
                         ▼
                    ┌─────────┐
                    │ Speaker │
                    │ Edge-TTS│
                    └─────────┘
```

---

## 📁 Project Structure

```text
AI-Desktop-Assistant/
│
├── app/
│   ├── assistant/
│   │   ├── assistant.py
│   │   └── command_processor.py
│   │
│   ├── commands/
│   │   ├── base.py
│   │   ├── router.py
│   │   ├── greeting_command.py
│   │   ├── time_command.py
│   │   ├── date_command.py
│   │   ├── search_command.py
│   │   ├── open_command.py
│   │   ├── play_command.py
│   │   ├── close_command.py
│   │   ├── window_command.py
│   │   ├── screenshot_command.py
│   │   ├── weather_command.py
│   │   ├── knowledge_command.py
│   │   ├── reminder_command.py
│   │   └── exit_command.py
│   │
│   ├── services/
│   │   ├── browser_service.py
│   │   ├── desktop_service.py
│   │   ├── music_service.py
│   │   ├── window_service.py
│   │   ├── screenshot_service.py
│   │   ├── time_service.py
│   │   ├── date_service.py
│   │   ├── weather_service.py
│   │   ├── knowledge_service.py
│   │   └── reminder_service.py
│   │
│   ├── speech/
│   │   ├── listener.py
│   │   └── speaker.py
│   │
│   ├── core/
│   │   └── data_manager.py
│   │
│   ├── utils/
│   │   ├── command_parser.py
│   │   └── logger.py
│   │
│   ├── data/
│   │   ├── apps.json
│   │   ├── websites.json
│   │   ├── music.json
│   │   └── memory.json
│   │
│   ├── config.py
│   └── main.py
│
├── assets/
├── screenshots/
├── roadmap.txt
├── requirements.txt
├── setup.py
├── .env.example
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies & Libraries

### Core
- `Python 3.12+`
- `SpeechRecognition`
- `Edge-TTS`
- `python-dotenv`

### Desktop Automation
- `psutil`
- `pygetwindow`
- `pyautogui`

### Browser & Media
- `webbrowser`
- `pygame`
- `pywhatkit`

### API & Networking
- `requests`

### Standard Python Libraries
- `datetime`, `json`, `logging`, `os`, `pathlib`, `subprocess`, `threading`

---

## ⚡ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/usman-dev56/Desktop-AI-Assistant.git
```

### 2. Enter the Project Directory
```bash
cd Desktop-AI-Assistant
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
```

### 4. Activate the Virtual Environment
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the project root based on `.env.example`:

```ini
ASSISTANT_NAME=Jarvis
WAKE_WORD=jarvis

VOICE_NAME=en-US-GuyNeural
VOICE_RATE=180
VOICE_VOLUME=1.0

DYNAMIC_ENERGY=True
ENERGY_THRESHOLD=300
PAUSE_THRESHOLD=0.8
LISTEN_TIMEOUT=5
PHRASE_TIME_LIMIT=8

OPENAI_API_KEY=
NEWS_API_KEY=
WEATHER_API_KEY=
```

> ⚠️ **Security Note:** Never upload your real `.env` file or API keys to GitHub. The `.env` file is excluded using `.gitignore`. Use `.env.example` as a safe configuration template.

---

## ▶️ Running the Assistant

From the project root:

```bash
python -m app.main
```

Jarvis will initialize:
1. Microphone
2. Speech recognition engine
3. Text-to-speech engine
4. Command processor & router
5. Desktop, browser, and media services

Then Jarvis will start actively listening for voice commands.

---

## 🎤 Example Commands

### 🖥️ Desktop Applications
- `Open Chrome`
- `Open Calculator`
- `Open Notepad`
- `Open Paint`
- `Open VS Code`

**Close applications:**
- `Close Chrome`
- `Close Notepad`
- `Close Calculator`

### 🪟 Window Management
- `Focus Chrome`
- `Minimize Chrome`
- `Maximize Chrome`
- `Restore Chrome`

**Supported aliases:**
- `Bring Chrome`
- `Activate Chrome`
- `Switch to Chrome`
- `Fullscreen Chrome`

### 🌐 Websites
- `Open Google`
- `Open YouTube`
- `Open GitHub`
- `Open LinkedIn`
- `Open Facebook`

### 🔎 Web Search
- `Search Python FastAPI tutorials`
- `Google machine learning`
- `Look up REST APIs`
- `Lookup Python decorators`
- `Find information about Django`

### 🎵 Music
- `Play Believer`
- `Play Faded`
- `Play Shape of You`
- `Play Perfect`
- `Play Unstoppable`
- `Play Relaxing Music`
- `Play Study Music`

### 📷 Screenshots
- `Screenshot`
- `Take Screenshot`
- `Capture Screen`
- `Capture Screenshot`

### 🕐 Time & Date
- `What time is it?` / `Tell me the time`
- `What is today's date?` / `Tell me today's date`

### 🌦️ Weather
- `Weather in Lahore`
- Retrieves: Temperature, Feels-like temperature, Humidity, Weather description, Country information.

### 👋 Exit
- `Exit`
- `Quit`
- `Goodbye`

---

## 🧩 Design Principles

The project follows a clean, modular architecture with clear separation of concerns:
- **Voice Input & Output:** Decoupled listener and speaker modules.
- **Command Pipeline:** Distinct stages for ingestion, normalization/parsing, and routing.
- **Service Layer:** Independent handler services for desktop, browser, media, and utilities.


---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork & clone the repository:
   ```bash
   git clone https://github.com/usman-dev56/Desktop-AI-Assistant.git
   ```
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "feat: Add new awesome feature"
   ```
4. Push to the branch and open a Pull Request.

---

## 📄 License

Distributed under the **MIT License**.

---

## 👨‍💻 Author

**Usman**  
- **GitHub:** [@usman-dev56](https://github.com/usman-dev56)

