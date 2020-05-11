import subprocess
import os
import datetime
import time
import speech_recognition as sr
import pyttsx3

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

def note(text):
	date=datetime.datetime.now()
	file_name=str(date).replace(":","-") + "-note.txt"
	with open(file_name,"w") as f:
		f.write(text)

	sublime='C:\Program Files\Sublime Text 3\sublime_text.exe'
	subprocess.Popen(['notepad.exe',file_name]) # Used to call notepad
	#subprocess.Popen([sublime,file_name]) #Used to call sublime

print("You may start speaking")
text=get_audio().lower()

NOTE_STRS= ["make a note","write this down","remember this"]
for phrase in NOTE_STRS:
	if phrase in text:
		speak("What would you like me to write down?")
		note_text= get_audio().lower()
		note(note_text)
		speak("I've made a note of that.")