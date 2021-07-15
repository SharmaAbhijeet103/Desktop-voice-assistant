import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\abhij\\OneDrive\\Desktop\\jarvis\\ss.png")

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your virtual assistant  Sir. How may i help you sir")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1                       # parameters for waiting for complete speech .
        audio = r.listen(source)                    # parameters such as energy can be changed as per loudness of surrounding.

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__=="__main__" :
    wishMe()
    while True:
      query = takeCommand().lower()                               # websites are in small alphabets to match
      # for tasks 
      if 'wikipedia' in query:                                   # condition to search wiki. 
            speak('Searching Wikipedia... please wait')
            query = query.replace("wikipedia", "")              #replacing wikipedia with what is in query.
            results = wikipedia.summary(query, sentences=3)      # whats coming for the result .
            speak("According to Wikipedia")
            print(results)
            speak(results)
      elif 'open youtube' in query:
            webbrowser.open("youtube.com")
      elif 'open google' in query:
            webbrowser.open("google.com")
      elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
      
      elif 'open zoom' in query:
            zoom_Path = "C:\\Users\\abhij\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoom_Path)
     
      elif 'screenshot' in query:
            screenshot()
            speak('screenshot has been taken')
      elif 'offline'in query:
            speak('have a good day sir bye bye thankyou')
            quit()

    