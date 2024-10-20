# Firstly import module for text to speech pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
text=input("Enter the text to convert into speech\n")
engine.say(text)
engine.runAndWait()