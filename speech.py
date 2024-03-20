import os

import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
speak("JAY SHRI RAM, AND LETS TALK")
while True:
    try:
        r=sr.Recognizer()
        # Use microphone as audio source
        with sr.Microphone() as source:
            r.pause_threshold=0.5
            print("Listening...")
            audio = recognizer.listen(source)

            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            #speak(text)
            #opening website
            sites=[["youtube","https://www.youtube.com"],["wikipedia",'https://www.wikipedia.com'],["google",'https://www.google.com']]
            for site in sites:
                if f"Open {site[0]}".lower() in text.lower():
                    speak(f"opening {site[0]}")
                    webbrowser.open(site[1])
            #todo: chage here to open any movie/song
            if "open movie".lower() in text.lower():
                movie="C:/Users/nsubh/Downloads/EP.18.v0.1639649397.720p.mp4"
                os.startfile(movie)

            # Example: Basic response (you can customize this)


    except sr.UnknownValueError:
        print("Could not understand audio, please repeat")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
