import speech_recognition as sr
import webbrowser
import datetime
import pyttsx3
import os

engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from SKI"

if __name__ == '__main__':
    print('Welcome to SKI A.I')
    say("SKI A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "Open music" in query:
            # Replace with the actual path to your music file
            musicPath = r"C:\Users\abish\Downloads\1$K1 - GODSLAYER [NCS Release].mp3"
            os.system(f"start {musicPath}")
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours and {minute} minutes")

        if "open Adobe".lower() in query.lower():
            # Replace with the actual path to your VLC shortcut or executable
            os.system(r"start C:\Users\abish\OneDrive\Desktop\abi.pdf")
