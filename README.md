# Text-To-Speech Converter

A simple cross-platform Python GUI application to convert text to spoken audio. It uses pyttsx3 for offline speaking (local TTS engines) and gTTS (Google Text-to-Speech) to save MP3 files.

Repository
- git clone https://github.com/Rajeshram2864/Text-To-Speech.git

Overview
- Enter or paste text into the textbox and choose a voice and speech rate.
- Click "Speak" to hear the text using the local TTS engine (pyttsx3).
- Click "Save Audio" to export the text to an MP3 file (gTTS — requires internet).
- Click "Play Last Audio" to open the saved file with the OS default player.

Features
- Offline speaking with selectable system voices (pyttsx3).
- Adjustable speech rate via a slider.
- Save output to MP3 using gTTS.
- Cross-platform playback (Windows, macOS, Linux).
- Minimal dependencies and a lightweight GUI (tkinter).

Prerequisites
- Python 3.8+ recommended
- Git (optional, for cloning)
- Internet connection required only for saving MP3 (gTTS)

Quick install (Windows)
1. Clone the repo:
   git clone https://github.com/Rajeshram2864/Text-To-Speech.git

2. Change to project directory:
   cd "Text -To-Speech"

3. (Optional) Create and activate a virtual environment:
   python -m venv .venv
   .venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

Run
- From the project folder:
  python text_to_speech_app.py

Output
<img width="828" height="658" alt="image" src="https://github.com/user-attachments/assets/a68e31cc-0abb-441b-934e-0a6db7d37c02" />


Files of interest
- text_to_speech_app.py — main application GUI and logic
- README.md — this document
- requirements.txt — Python dependencies

How the app works (high level)
- pyttsx3 is initialized and available system voices are enumerated for the voice selection menu.
- Speaking uses pyttsx3.setProperty('voice') and .say/.runAndWait for offline playback.
- Saving uses gTTS to generate an MP3 file because pyttsx3 does not reliably export MP3.
- The app stores the last saved file path so it can be opened by the OS default audio player.

Troubleshooting
- No voices shown / different voices: pyttsx3 uses platform TTS engines (SAPI5 on Windows, NSSpeechSynthesizer on macOS, eSpeak on some Linux distros). Install or enable system voices if none are available.
- gTTS ImportError: install dependencies with pip install -r requirements.txt.
- gTTS failing to save: requires internet access and may be subject to Google API limits.
- MP3 playback fails to open: ensure your OS has an associated application for .mp3 files. On some Linux systems, install xdg-utils or a desktop audio player.

Testing tips
- Use short sample texts first to verify voice selection and rate.
- Save to a temporary folder to verify MP3 creation and playback.
- If pyttsx3 speaks but saved MP3 is silent/invalid, verify gTTS usage and internet connectivity.

Security & privacy
- Text saved using gTTS is sent to Google servers; do not send sensitive data if privacy is a concern.
- All local speaking via pyttsx3 remains on your machine.

Known limitations
- gTTS requires internet and uses Google servers.
- pyttsx3 does not support direct MP3 export.
- Voice availability and quality depend on the OS and installed voices.

Contributing
- Issues and pull requests are welcome. Fork the repo, create a feature branch, and submit a PR.
- Keep changes focused: dependency updates, better error handling, packaging (exe), or additional export formats.

Packaging (optional)
- Use PyInstaller to create a standalone executable:
  pip install pyinstaller
  pyinstaller --onefile text_to_speech_app.py

License
- Add your preferred license. (No license file is included by default.)

Acknowledgements
- pyttsx3 — offline TTS engine wrapper
- gTTS — Google Text-to-Speech library
- tkinter — Python standard GUI toolkit

Contact
- For improvements, open an issue in the repository.
#

