import speech_recognition as sr
import pyttsx3
import datetime
from time import ctime 
import webbrowser
import os
import PySimpleGUI as sg
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def audio_rec(want=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if want:
           speak(want)
        audio=r.listen(source)
        voice_data= " "
        try:
            voice_data=r.recognize_google(audio,language="en")
        except sr.UnknownValueError:    
            speak("Sorry, Can you repeat that ")
        return voice_data

def respondA(voice_data):
    if "hello" in  voice_data:
        speak("Hi! Do you want me to do something for you?")
    elif "hey" in  voice_data:
        speak("Hi! Do you want me to do something for you?")
    elif "hi" in  voice_data:
        speak("Hi! Do you want me to do something for you?")
    elif "heyyo" in  voice_data:
        speak("Hi! Do you want me to do something for you?")
    elif "what is your name" in voice_data:
        speak('My name is Kiki')
    elif "what time is it" in voice_data:
        speak(ctime())
    elif "how are you" in voice_data:
        speak("I am very well, thanks for asking")
    elif "how you doing" in voice_data:
        speak("I am very well, thanks for asking")
    elif "search" in voice_data:
        #search=audio_rec("What do you want to do search?")
        voice_data= voice_data.replace("search", "")
        url="https://google.com/search?q=" + voice_data
        webbrowser.get().open(url)
        speak(voice_data)
    elif "find location" in voice_data:
        #location=audio_rec("Which location do you want to find?")
        voice_data= voice_data.replace("find location", "")
        url="https://google.nl/maps/place/" +voice_data + "/&amp;"
        webbrowser.get().open(url)
        speak(voice_data)
    elif "make a joke" in voice_data:
        speak("What does a baby computer call his father? Data")
    elif "youtube" in voice_data:
        voice_data= voice_data.replace("youtube", "")
        url="https://www.youtube.com/results?search_query=" +voice_data 
        webbrowser.get().open(url)
        speak(voice_data)
    elif "do you love me" in voice_data:
        speak("Say you'll never ever leave from beside me")
        webbrowser.get().open("https://www.youtube.com/watch?v=3WSgJCYIewM")
    elif "google" in voice_data:
        webbrowser.get().open("https://google.com/")
        speak("enjoy!")
    elif "play music" in voice_data:
        webbrowser.get().open("http://radio.garden")
        speak("enjoy!")
    elif "twitter" in voice_data:
        webbrowser.get().open("http://twitter.com/")
        speak("enjoy!")
    elif "facebook" in voice_data:
        webbrowser.get().open("http://facebook.com/")
        speak("enjoy!")
    elif 'wikipedia' in voice_data:  #if wikipedia found in the query then this block will be executed
        speak('Searching Wikipedia...')
        voice_data= voice_data.replace("wikipedia", "")
        answer = wikipedia.summary(voice_data, sentences=2) 
        speak("According to Wikipedia")
        #print(results)
        speak(answer)
           
def respondT(values1):
    if "what is your name" in values1:
        return "My name is Kiki"
    elif "do you love me" in values1:
        url = "https://www.youtube.com/watch?v=3WSgJCYIewM"
        webbrowser.get().open(url)
        return "Say you'll never ever leave from beside me"
    elif "play music" in values1:
        url = "http://radio.garden"
        webbrowser.get().open(url)
        return "enjoy!"
    elif "twitter" in values1:
        url = "http://twitter.com"
        webbrowser.get().open(url)
        return "enjoy!"
    elif "facebook" in values1:
        url = "http://facebook.com"
        webbrowser.get().open(url)
        return "enjoy!"
    elif "what time is it" in values1:
        answer=ctime()
        return answer
    elif "how are you" in values1:
        return "I am very well, thanks for asking"
    elif "how you doin" in values1:
        return "I am super good, thanks for asking"
    elif "make a joke" in values1:
        return "What does a baby computer call his father?\nData"
    elif "hello" in values1:
        return "Hi! Do you want me to do something for you?"
    elif "hey" in values1:
        return "Hi! Do you want me to do something for you?"
    elif "hi" in values1:
        return "Hi! Do you want me to do something for you?"
    elif "heyyo" in values1:
        return "Hi! Do you want me to do something for you?"
    elif "bye bye" in values1:
        speak("See you again")
        exit()
            
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning" + "...")
    elif hour>=12 and hour<18:
        speak("Good Afternoon"  + "...")
    else:
        speak("Good Evening"  + "...")
    speak("How may I help you?...")

sg.change_look_and_feel('Purple')

# Window 1 layout
menu_def = [['&Help', ['&Commands',[" &TEXT","---","&AUDIO"],"&About"]]]
layout = [
            [sg.Text('Do you want to use it as text or audio?'),sg.Text('     ', key='-OUTPUT-')],
            [sg.Text('')],
            [sg.Button('Text'), sg.Button('Audio'),sg.Text("                                "), sg.Button('Exit',button_color=('white', 'red'))],
            [sg.Menu(menu_def)]
         ]

window = sg.Window('Welcome to Kiki', layout,icon="icon.ico")
win2_active = False
i=0
while True:             # Event Loop
    event, values = window.read(timeout=100)
    
    if event== " TEXT":
        sg.Popup(">some greetings like hello,hi,hey",
                 ">what is your name",
                 ">how are you or how you doing",
                 ">what time is it",
                 ">play music",
                 ">twitter and facebook",
                 ">click 'Search in Google' for searching",
                 ">click 'Find Location' to open map",
                 ">click 'Wikipedia' to search something in Wikipedia",
                 ">make a joke",
                 ">do you love me",
                 title="Text Commands",icon="icon.ico",non_blocking=True
                )       
    if event=="AUDIO":
            sg.Popup(">Some greetings like hello,hi,hey",
                     ">What is your name",
                     ">How are you or how you doing",
                     ">What time is it",
                     ">Play music",
                     ">Open 'Google','Youtube','Facebook','Twitter'",
                     ">Make a joke",
                     ">Do you love me",
                     ">To search something in Wikipedia,firstly say 'wikipedia' and then say whatever you want",
                     ">To find location,firstly say 'find location' and then say somewhere to find",
                     ">To search something,firstly say 'search' and then say whatever you want",
                     title="Audio Commands",icon="icon.ico",non_blocking=True
                     )
    if event=="About":
        sg.Popup("© 2020 I.Kaan Ozay -KIKI- All Rights Reserved",title="Copyright",icon="icon.ico",non_blocking=True)
    if event in (None, 'Exit'):
        break
    if event == 'Text' and not win2_active:     
        win2_active = True 
        layout2 = [ #window2 layout
            [sg.Text('How can I help you?')],
            [sg.Input('', key='-IN-'),sg.Button('Okay',button_color=('black', 'white'))],
            [sg.Button('Search in Google'),sg.Button('Wikipedia'),sg.Button('YouTube'),sg.Button('Find Location')],
            [sg.Text('                                                                      ', size=(45,8),key='-OUTPUT-')],
            [sg.Button('Back',button_color=('white', 'red'))],
            [sg.Menu(menu_def)]
            ]

        window2 = sg.Window('Kiki', layout2,icon="icon.ico") 

    if win2_active:
        event, values = window2.read(timeout=100)
        if event== " TEXT":
            sg.Popup(">some greetings like hello,hi,hey",
                     ">what is your name",
                     ">how are you or how you doing",
                     ">what time is it",
                     ">play music",
                     ">twitter and facebook",
                     ">click search in google for searching",
                     ">click find location to open map",
                     ">click 'Wikipedia' to search something in Wikipedia",
                     ">make a joke",
                     ">do you love me",
                     title="Text Commands",icon="icon.ico",non_blocking=True
                     ) 
        elif event=="AUDIO":
            sg.Popup(">Some greetings like hello,hi,hey",
                     ">What is your name",
                     ">How are you or how you doing",
                     ">What time is it",
                     ">Play music",
                     ">Open 'Google','Youtube','Facebook','Twitter'",
                     ">Make a joke",
                     ">Do you love me",
                     ">To search something in Wikipedia,firstly say 'wikipedia' and then say whatever you want",
                     ">To find location,firstly say 'find location' and then say location",
                     ">To search something,firstly say 'search' and then say whatever you want",
                     title="Audio Commands",icon="icon.ico",non_blocking=True
                     )
        elif event=="About":
            sg.Popup("© 2020 I.Kaan Ozay -KIKI- All Rights Reserved",title="Copyright",icon="icon.ico",non_blocking=True)
        elif event == 'Back' or event is None:
            win2_active = False
            window2.close()
        elif event == 'Okay':
            myDict=values["-IN-"]
            answer=respondT(myDict)
            speak(answer)
            window2["-OUTPUT-"].update(answer)
        elif event=="Search in Google":
            url="https://google.com/search?q=" + values["-IN-"]
            webbrowser.get().open(url)
        elif event=="Find Location":
            url="https://google.nl/maps/place/" +values["-IN-"] + "/&amp;"
            webbrowser.get().open(url)
        elif event=="YouTube":
            url = "https://www.youtube.com/results?search_query="+ values["-IN-"]
            webbrowser.get().open(url)
        elif event=='Wikipedia':  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            values["-IN-"]= values["-IN-"].replace("wikipedia", "")
            answer = wikipedia.summary(values["-IN-"], sentences=2) 
            speak("According to Wikipedia")
            speak(answer)
            window2["-OUTPUT-"].update(answer)
           
    if event == 'Audio':
        if i==0:
            wishMe()
            i=1

        voice_data=audio_rec().lower()
        respondA(voice_data)
            
     
window.close()