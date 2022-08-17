from datetime import datetime
import smtplib
import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) # says text
    engine.runAndWait()
# speak("Hello Sir I am Shaurya! How may I help You Today")
def time():
    Time = datetime.datetime.now().strftime("%H hours %M minutes %S seconds")
    speak("The time right now is" + Time)
# time()
def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    month_name = ["","january","February","March","April","May","June","July","August","September","October","November","December"]
    day = (datetime.datetime.now().day)
    # speak(date)
    # speak(month)
    # speak(year)
    speak("today is" + str(day) + month_name[month] + str(year))
# date()
def greet():
    speak("Welcome Back Sir! ")
    time()
    date()
    hour = int(datetime.datetime.now().hour)
    if (hour>=6 and hour<12):
        speak("Good Morning Sir!")
    elif(hour>=12 and hour<17):
        speak("Good Afternoon Sir!")
    elif(hour>=18 and hour<22):
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("I am at your Service. please tell me how may I help you")
# greet()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) #useful for microphone
        audio = r.listen(source,timeout=8,phrase_time_limit=8) # useful for helping microphone get speech (last 2 arguments)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)

        print("say that again please...")
        return "None"
    return query

def sendEmail(receiver_id,content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivangnov@gmail.com','aman1108*')
    server
if __name__ == "__main__":
    # greet()
    
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'hello' in query:
            speak("hello! how may I help you?")
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("who should I send this to?")
                receiver_id = takeCommand()
                sendEmail(receiver_id,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir , I am unable to send this email at the moment")    
        elif 'open youtube' in query:
            wb.open('https://'+"youtube.com")
            query.replace("open youtube","https://youtube.com")
        elif 'open twitter' in query:
            wb.open('https://'+"twitter.com")
            query.replace("open twitter","https://twitter.com")
        elif 'open reddit' in query:
            wb.open('https://'+"reddit.com")
            query.replace("open reddit","https://reddit.com")
        elif 'open github' in query:
            wb.open("https://"+"github.com")
            query.replace("open github","https://github.com")
        elif 'open linkedin' in query:
            wb.open("https://"+"linkedin.com")
            query.replace("open linkedin","https://linkedin.com")
        elif 'open google' in query:
            wb.open("www.google.com")
            query.replace("open google","https://google.com")
        elif 'open stack overflow' in query:
            wb.open("https://"+"stackoverflow.com")
            query.replace("open stackoverflow","https://stackoverflow.com")
        elif 'open spotify' in query:
            wb.open("https://"+"spotify.com")
            query.replace("open spotify","https://spotify.com")
        elif 'open codechef' in query:
            wb.open("https://"+"codechef.com")
            query.replace("open codechef","https://codechef.com")
        elif 'open codeforces' in query:
            wb.open("https://"+"codeforces.com")
            query.replace("open codeforces","https://codeforces.com")
        elif 'open netflix' in query:
            wb.open("https://"+"netflix.com")
            query.replace("open netflix","https://netflix.com")
        elif 'open amazon prime videos' in query:
            wb.open('https://'+"primevideo.com")
            query.replace("open amazon prime videos","https://primevideo.com")
        elif 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'open vs code' in query:
            vscodepath = "--------------------------------------------------"
            os.startfile(vscodepath)
