#  python.exe main.py

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d093053d72bc40248998159804e0e67d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://feacbook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")  
    elif "open weather app" in c.lower():
        webbrowser.open("file:///C:/Users/dkc63/Desktop/Weather%20App/index.html")    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    # elif "news" in c.lower():
    #         r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apikey={newsapi}")
    #         if r.status_code ==200:
    #             data = r.json()

    #             articles = data.get('articles',[])
    #             for article in articles:
    #                  speak(article['title'])

    elif "stop" in c.lower():
        speak("good by")                 
        exit()


    print(c)          


if __name__ =="__main__":
    speak("Initializing Jarvis.....")
    while True:
        r=sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=3,phrase_time_limit=4)
                word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis Activated..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error :",e) 
                      




