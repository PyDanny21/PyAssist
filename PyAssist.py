import datetime
import json
import time
import vosk
import pyaudio
import subprocess as sp
import wikipedia
import speech_recognition as sr
import pytube
import requests
import cv2
import pyttsx3
#import pywhatkit as kit
import pyautogui
import random
from sketchpy import library as lib
import calendar
import win32api
#normal conversation

import os
opening_text=['on it,sir','okay sir,i am working on it']
#maths calculation
import pynput
from vosk import Model,KaldiRecognizer

p=pyttsx3.init('sapi5')
voices=p.getProperty('voices')
p.setProperty('voice',voices[2].id)
p.setProperty('rate',190)
p.setProperty('volume',1.0)

def speak(audio):
    p.say(audio)
    p.runAndWait()

#speak('hi sir')

def greetings():
    hr=int(datetime.datetime.now().hour)
    if hr>=6 and hr<12:
        speak('Good morning sir!')
    elif hr>=12 and hr<16:
        speak('Good Afternoon sir!')
    else:
        speak('Good evening sir!')
#greetings()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(random.choice(opening_text))
        else:
            hour = datetime.datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Unable to recognize your voice, sir')
        query = 'None'
    return query


paths = {
    'notepad': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
def open_notepad():
    os.startfile(paths['notepad'])


def open_calculator():
    os.startfile(paths['calculator'])

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_cmd():
    os.system('start cmd')

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=4)
    print(results)
    speak(results)
    return results

def note():
    from pynput.keyboard import Controller
    key = Controller()
    speak('sir,please what should i write')
    nn = input(':')
    speak('sir,please should i include date and time?')
    datetimer = input(':')
    with open('log.txt','a') as file:
        time = datetime.datetime.now().strftime('%H:%M')
        date = datetime.datetime.now().date()
        if 'yes' in datetimer:
            file.write(f'on {date} at {time},you made a note saying {nn}')

        elif 'no' in datetimer:
            file.write(f'you made a note saying {nn}')
        speak('Note made successfully!')


def open_note():
    os.startfile('C:\\Users\\User\\PycharmProjects\\pythonProject\\log.txt')


def play_music():
    music_dir = 'C:\\Users\\User\\Desktop\\P.L.A.Y.L.I.S.T\\'
    songs = os.listdir(music_dir)
    # print(len(songs))
    song = songs[random.randint(0, 63)]
    speak(f'Playing {song}')
    title = os.startfile(music_dir + song)


def play_movie():
    movies_dir = 'C:\\Users\\User\\movies\\'
    movies = os.listdir(movies_dir)
    # print(len(movies))
    mov = movies[random.randint(0, 51)]
    speak(f'Playing {mov}')
    os.startfile(movies_dir + mov)


def speak_note():
    with open('log.txt','r') as ff:
        a = ff.read()
        speak(a)


def switch():
    time.sleep(0.5)
    pyautogui.hotkey('alt','tab')
    speak('window switched')

def screenshot():
    time.sleep(1)
    pyautogui.hotkey('win','prtsc')

def minimize_windows():
    time.sleep(1)
    pyautogui.hotkey('win','m')
    speak('all windows minimized')

def maximize():
    time.sleep(1)
    pyautogui.hotkey('win','shift','m')
    speak('all windows maximized')

def draw():
    a=lib.rdj()
    a.draw()

def calenda():
    speak('which year please?')
    year=int(input(':'))
    speak(f'sir,please here is the calendar for {year}')
    print(calendar.calendar(year))


def hackmyphone(ip_address):
    capture = cv2.VideoCapture(f"http:{ip_address}:8080/video")
    while True:
        success, frame = capture.read()

        cv2.imshow('Phone Camera', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    speak('Activating system configuration. Pulling all necessary requests. ')
    speak('')
    speak('I am online and ready')
    greetings()
    speak('I am Pi, your personal assistant')
    speak('please,how may i help you')
    while True:
        command=input('USER SAID:')
        if 'minimize' in command:
            minimize_windows()

        elif 'maximize' in command:
            maximize()

        elif 'calendar' in command:
            speak('on it sir')
            calenda()

        elif 'notepad' in command:
            speak(random.choice(opening_text))
            open_notepad()

        elif 'cmd' in command:
            speak(random.choice(opening_text))
            open_cmd()

        elif 'camera' in command:
            speak(random.choice(opening_text))
            open_camera()

        elif 'calculator' in command:
            speak(random.choice(opening_text))
            open_calculator()

        elif 'screenshot' in command:
            speak(random.choice(opening_text))
            screenshot()

        elif 'switch window' in command:
            speak(random.choice(opening_text))
            switch()

        elif 'shutdown' in command:
            speak(random.choice(opening_text))
            os.system('shutdown /s')

        elif 'restart' in command:
            speak(random.choice(opening_text))
            os.system('shutdown /r')

        elif 'lock screen' in command:
            speak(random.choice(opening_text))
            os.system('shutdown /l')

        elif 'open youtube' in command:
            speak(random.choice(opening_text))
            sp.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe','www.youtube.com'])

        elif 'open google' in command:
            speak(random.choice(opening_text))
            sp.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe','www.google.com'])

        elif 'visit' in command:
            speak(random.choice(opening_text))
            web=command.replace('visit','')
            sp.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe',f'{web}'])

        elif 'open stackoverflow' in command:
            speak(random.choice(opening_text))
            sp.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe','www.stackoverflow.com'])

        elif 'open wikipedia' in command:
            speak(random.choice(opening_text))
            sp.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe','www.wikipedia.com'])

        elif 'search wikipedia' in command:
            query=command.replace('search wikipedia','')
            speak(f'searching for {query} from wikipedia')
            search_on_wikipedia(query)

        elif 'draw' in command:
            speak(random.choice(opening_text))
            draw()

        elif 'search for' in command:
            a=command.replace('search for' or 'search','')
            speak(f'searching for {a} from google')
            sp.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe',f'https://www.google.com/search?client=firefox-b-d&q={a}'])

        elif 'make note' in command:
            speak(random.choice(opening_text))
            note()

        elif 'show note' in command:
            speak(random.choice(opening_text))
            open_note()

        elif 'speak note' in command:
            speak(random.choice(opening_text))
            speak_note()

        elif 'play music' in command:
            speak(random.choice(opening_text))
            play_music()

        elif 'movie' in command:
            speak(random.choice(opening_text))
            play_movie()

        elif 'music studio' in command:
            speak(random.choice(opening_text))
            sp.Popen(['C:\\Program Files\\Image-Line\\FL Studio 20\\FL64.exe'])

        elif 'hack my camera' in command:
            speak(random.choice(opening_text))
            speak('sir,please type your ip address')
            ipaddress=input('USER SAID:')
            speak('hacking your mobile phone camera')
            hackmyphone(ipaddress)


        elif 'obs studio' in command:
            speak(random.choice(opening_text))
            os.startfile('C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe')
        speak('sir,please what should i do again.')




'''        elif 'search youtube' in command:
            speak(random.choice(opening_text))
            video=command.replace('search youtube','')
            try:
                kit.playonyt(video)
            except:
                speak('network error, sir')
'''
#minimize_windows()
#time.sleep(3)
#maximize()
#search_on_wikipedia('how to cook')

'''def play_on_youtube(video):
    kit.playonyt(video)
#play_on_youtube('programming')

def search_on_google(query):
    kit.search(query)
#search_on_google('python')
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
#send_whatsapp_message('0550457619','hello')
'''


'''
model=Model("vosk\\vosk-model-small-en-us-0.15")
recognizer=KaldiRecognizer(model,16000)
mic=pyaudio.PyAudio()
stream=mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)

while True:
    data=stream.read(4096,exception_on_overflow=False)
    if len(data)==0:
        break
    if recognizer.AcceptWaveform(data):
          rec=recognizer.Result()
          command=json.loads(rec)
          print('\t\t\t\t\t\t\t\t\t\t\t\t\t:'+command['text'])
          if 'hello' in command['text']:
              stream.stop_stream()
              print('\t\t\t\t\t\t\t\t\t\t\t\t\t'+command['text'])
              speak('Hi sir, I am Py assist,your personal assistant')
              speak('How may i help you?')
              stream.start_stream()
              print('')
              print('Listening')
              print('')

'''