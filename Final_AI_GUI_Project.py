import os
from gtts import gTTS
import speech_recognition as sr
import tkinter as tk
from tkinter import ttk, messagebox

# Function to convert text to speech
def text_to_speech(text, filename="output.mp3"):
    if text.strip() == "":
        messagebox.showerror("Error", "No text to speak")
        return
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"start {filename}")  # or Windows, use 'afplay' for Mac, and 'mpg321' for Linux

# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "Could not understand audio"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "Error requesting results"

# Function to handle Text to Speech conversion from the UI
def text_to_speech_ui():
    text = text_entry.get()
    text_to_speech(text)

# Function to handle Speech to Text conversion from the UI
def speech_to_text_ui():
    text = speech_to_text()
    if text:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, text)
        output_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Text to Speech and Speech to Text")

# Create a styled frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0)

# Create a styled label and entry box
ttk.Label(frame, text="Enter text to Convert:").grid(row=0, column=0)
text_entry = ttk.Entry(frame, width=80)
text_entry.grid(row=0, column=1)

# Create styled buttons
tts_button = ttk.Button(frame, text="Convert Text to Speech", command=text_to_speech_ui)
tts_button.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.W+tk.E)

stt_button = ttk.Button(frame, text="Convert Speech to Text", command=speech_to_text_ui)
stt_button.grid(row=2, column=0, columnspan=2, pady=10, sticky=tk.W+tk.E)

# Create a Text widget to display speech-to-text output
ttk.Label(frame,text="Speech Output").grid(row=3,column=0,pady=5)
output_text = tk.Text(frame, wrap=tk.WORD, width=60, height=6, state=tk.DISABLED)
output_text.grid(row=3, column=1,pady=10)

# Run the GUI event loop
root.mainloop()
 