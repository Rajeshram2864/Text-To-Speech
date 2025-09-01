"""
Text-to-Speech Converter Application
------------------------------------

This is a Python application with a simple graphical user interface (GUI) for converting text to speech.
It uses the pyttsx3 library for offline speech synthesis to speak text aloud with selectable voices and speech rates.
It uses the gTTS (Google Text-to-Speech) library to save audio in MP3 format.

Features:
- Enter text in a text box.
- Select between available voices installed on the system.
- Adjust speech rate using a slider.
- Speak the text aloud with the selected voice and rate.
- Save the spoken audio as an MP3 file.
- Play the last saved audio file.
- Cross-platform support (Windows, macOS, Linux).

Requirements:
- Python 3.x
- Libraries: pyttsx3, gTTS, tkinter (comes with Python)
- Install required libraries using:
    pip install pyttsx3 gTTS

Usage:
- Run this script.
- Enter or paste text into the text box.
- Select desired voice and speech rate.
- Click "Speak" to hear the text.
- Click "Save Audio" to save as MP3.
- Click "Play Last Audio" to play the saved file.

Note:
- Saving in WAV format is not supported due to library limitations.
- gTTS requires internet connection to save MP3.

"""

import pyttsx3
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import platform
import subprocess

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Text to Speech Converter")
        master.geometry('600x450')

        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')

        # Instructions label
        self.label = tk.Label(master, text="Enter text to convert to speech:")
        self.label.pack(pady=10)

        # Text input area
        self.text_entry = tk.Text(master, height=10, width=70)
        self.text_entry.pack(pady=10)

        # Voice selection label and dropdown
        self.voice_label = tk.Label(master, text="Select Voice:")
        self.voice_label.pack()
        self.voice_var = tk.StringVar(master)
        voice_names = [voice.name for voice in self.voices]
        if voice_names:
            self.voice_var.set(voice_names[0])
        self.voice_menu = tk.OptionMenu(master, self.voice_var, *voice_names)
        self.voice_menu.pack(pady=5)

        # Speech rate label and scale
        self.rate_label = tk.Label(master, text="Select Speech Rate:")
        self.rate_label.pack()
        self.rate_var = tk.IntVar(master)
        self.rate_var.set(150)  # Default speech rate
        self.rate_scale = tk.Scale(master, from_=50, to=300, orient='horizontal', variable=self.rate_var)
        self.rate_scale.pack(pady=5)

        # Buttons for Speak, Save, and Play
        self.speak_button = tk.Button(master, text="Speak", width=20, command=self.speak_text)
        self.speak_button.pack(pady=5)

        self.save_button = tk.Button(master, text="Save Audio", width=20, command=self.save_audio)
        self.save_button.pack(pady=5)

        self.play_button = tk.Button(master, text="Play Last Audio", width=20, command=self.play_audio)
        self.play_button.pack(pady=5)

        # Store last saved audio file path for playing
        self.last_audio_path = None

    def speak_text(self):
        text = self.text_entry.get('1.0', tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter some text to speak.")
            return

        # Set the selected voice for pyttsx3 engine
        selected_voice_idx = next((i for i, voice in enumerate(self.voices) if voice.name == self.voice_var.get()), 0)
        self.engine.setProperty('voice', self.voices[selected_voice_idx].id)

        # Set speech rate
        self.engine.setProperty('rate', self.rate_var.get())

        # Speak text aloud
        self.engine.say(text)
        self.engine.runAndWait()

    def save_audio(self):
        text = self.text_entry.get('1.0', tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter some text to save.")
            return

        # Ask user for location to save file
        file_path = filedialog.asksaveasfilename(defaultextension='.mp3',
                                                 filetypes=[("MP3 files", '*.mp3')],
                                                 title="Save audio as...")
        if not file_path:
            return

        # Use gTTS for saving MP3 because pyttsx3 does not support saving audio files
        try:
            from gtts import gTTS
        except ImportError:
            messagebox.showerror("Import Error", "gTTS library not found. Install with:\n\npip install gTTS")
            return

        try:
            tts = gTTS(text)
            tts.save(file_path)
            messagebox.showinfo("Success", f"Audio saved successfully at:\n{file_path}")
            self.last_audio_path = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save audio:\n{str(e)}")


    def play_audio(self):
        if not self.last_audio_path or not os.path.isfile(self.last_audio_path):
            messagebox.showerror("Error", "No saved audio file found. Please save audio first.")
            return

        try:
            # Cross-platform audio playing
            if platform.system() == 'Windows':
                os.startfile(self.last_audio_path)
            elif platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', self.last_audio_path))
            else:  # Linux and others
                subprocess.call(('xdg-open', self.last_audio_path))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to play audio:\n{str(e)}")


if __name__ == '__main__':
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
