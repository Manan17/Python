import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afernoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis an Iron Man's creation")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said = ",query)

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query
      
if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching in wikipedia")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open instagram' in query:
        webbrowser.open("instagram.com")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
    
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    
    elif 'play music' in query:
        music_dir = 'F:\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[2]))


    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
        print(time)
