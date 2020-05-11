import speech_recognition as sr
import pyttsx3
import os, time

def speak(text):
	
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		audio=r.listen(source)
		said=""
		
		try:
			said=r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception:"+str(e))
	return said

text=get_audio()

if "hello" in text:
	speak("Hello Saurabh, how are you?")

if "what is my name" in text:
	speak("Your name is Saurabh Agarwal")
