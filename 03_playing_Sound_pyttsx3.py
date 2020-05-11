import speech_recognition as sr
import pyttsx3
import os, time

def speak(text):
	
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("Hello Saurabh")