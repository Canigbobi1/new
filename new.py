#!/usr/bin/env python3
import wolframalpha
client = wolframalpha.Client("")

import speech_recognition as sr
import wikipedia
import PySimpleGUI as sg
import pyttsx3


sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.

layout = [ [sg.Text('Enter command'), sg.InputText()],
            [sg.Button('Search'), sg.Button('Exit')] ]


# Create the Window
window = sg.Window('BlacTechs Assistant', layout)
# Event Loop to process "events" and get the "values" of the inputs
def speak(string):
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()
speak("Welcome back Mr. Blac, How can I help you ?")
speak("Please enter what you need me to get for you")

while True:
    event, values = window.read()
    if event in (None, "Cancel"):
        break
    res = client.query(values[0])
    wolfram_res = next(res.results).text
    wiki_res = wikipedia.summary(values[0], sentences = 3)
    
    import pyttsx3
    engine = pyttsx3.init()
    sg.PopupNonBlocking("wikipedia result is : " +wiki_res, "wolfram result is : " +wolfram_res)
    engine.say(wiki_res)
    engine.say(wolfram_res)
    engine.runAndWait()
    
    speak("click on the ok button to close this window")
    speak("after that input a new command or click the exit button")
    print(values[0])
    

window.close()
