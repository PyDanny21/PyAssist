import speech_recognition as sr
import pyttsx3
from googlettrans import Translator
pt=pyttsx3.init('sapi5')
r=sr.Recognizer()
def recognizer():
    with sr.Microphone() as source:
        print('Speak now')
        audio=r.listen(source)
        speech_text=r.recognize_google(audio)
        print(speech_text)

voices=pt.getProperty('voices')
pt.setProperty('voice',voices[1].id)

def speak(text):
    pt.say(text)

    pt.runAndWait()

speak('kelvin')



translator=Translator()
translator.translate(recognizer,dest='in')