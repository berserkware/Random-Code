import speech_recognition as sr
import pyttsx3

r = sr.Recognizer() 

mic = sr.Microphone()

with mic as source:
  audio = r.listen(source)

engine = pyttsx3.init()

engine.say(r.recognize_google(audio))

engine.runAndWait()