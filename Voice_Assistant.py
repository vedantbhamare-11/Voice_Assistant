import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import pytz
import subprocess
import tkinter as tk

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: ", str(e))
    
    return said

def search_google(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)
    speak("Here's what I found for " + query)

def get_location():
    url = "https://www.google.com/maps/search/?api=1&query=" + "current location"
    webbrowser.open(url)
    speak("Here's your current location")






def find_files(name):
    path = "/"
    results = []
    for root, dirs, files in os.walk(path):
        if name in files:
            results.append(os.path.join(root, name))
    if results:
        speak("I found these files:")
        for result in results:
            print(result)
            speak(result)
    else:
        speak("Sorry, I couldn't find any files with that name.")

def set_reminder(reminder):
    tz = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(tz)
    speak(f"Reminder set for {reminder} at {current_time.hour} hours {current_time.minute} minutes")
    with open('reminders.txt', 'a') as file:
        file.write(f"{reminder}\t{current_time}\n")

speak("Hi! How can I help you?")
while True:
    text = get_audio().lower()
    if "hello" in text:
        speak("Hi! How are you?")
    elif "goodbye" in text:
        speak("Goodbye!")
        break
    elif "search" in text:
        speak("What do you want me to search for?")
        query = get_audio()
        search_google(query)
    elif "location" in text:
        get_location()
    elif "find" in text and "file" in text:
        speak("What is the name of the file you want me to find?")
        name = get_audio()
        find_files(name)
    elif "set" in text and "reminder" in text:
        speak("What do you want me to remind you of?")
        reminder = get_audio()
        set_reminder(reminder)
    elif "open" in text and "file explorer" in text:
        subprocess.Popen('explorer.exe')
        speak("Opening File Explorer")
    else:
        speak("Sorry, I didn't understand that.")