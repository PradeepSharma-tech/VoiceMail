import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak('GOOD MORNING Sir!')
    elif hour>=12 and hour<16:
        speak('Good AfterNoon Sir!')
    else:
        speak("Good Evening Sir!")

    speak(' I am Vector your assistant! and How may i help you')

def takeCommand():
    # It wil take command input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening.")
        print("Listening.....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        speak("Recognizing.....")
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print('Say that again please..')
        return "NONE"
    return query

def sendmail(to,content):
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('sender mail','sender password')
    mail.sendmail('receiver mail',to,content)
    mail.close()

if __name__ == '__main__':
     wishme()
     while True:

        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open('youtube.com')
        
        elif "open google" in query:
            webbrowser.open('google.com')
    
        elif "open stackoverflow" in query:
              webbrowser.open('stackoverflow.com')
            
        
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%Hour:%Minutes")
            speak(f"Sir,the time is {strTime} ")
        
         
        elif "open gmail" in query:
             webbrowser.open('gmail.com')
        
        elif "shutdown" in query:
             speak("okay Have a nice day sir")
             exit()
        
        elif "send email" in query:
            try:
                speak("What should i write")
                content=takeCommand() 
                speak("your message has been written,please tell me whom you want to send this  ")
                mail=takeCommand()
                space=mail.replace("dot",".")
                to=space.replace(" ","")
                sendmail(to.lower(),content)
                print("Email has been sent")
                speak("Email has been sent")
                    

            except Exception as e:
                print(e)
                speak("Sorry i am unable to send this email")
        
        
