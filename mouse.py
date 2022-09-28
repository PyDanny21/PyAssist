'''import mediapipe as mp
import cv2

cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
while(True):
    _,frame=cap.read()
    rgb_frame=cv2.cvtColor(frame,cv2.BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    cv2.imshow('Virtual_Camera',frame)
    if cv2.waitKey(1)==ord('q'):
        break'''
import random
import pyautogui
import pyttsx3
import os
import datetime
p=pyttsx3.init('sapi5')
voices=p.getProperty('voices')
p.setProperty('voice',voices[2].id)
p.setProperty('rate',190)
p.setProperty('volume',1.0)

def speak(audio):
    p.say(audio)
    p.runAndWait()


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


def speak_note():
    with open('log.txt','r') as ff:
        a = ff.read()
        speak(a)
def play_music():
    music_dir='C:\\Users\\User\\Desktop\\P.L.A.Y.L.I.S.T\\'
    songs=os.listdir(music_dir)
    #print(len(songs))
    song=songs[random.randint(0,63)]
    speak(f'Playing {song}')
    title=os.startfile(music_dir+song)


def play_movie():
    movies_dir='C:\\Users\\User\\movies\\'
    movies=os.listdir(movies_dir)
    #print(len(movies))
    mov=movies[random.randint(0,51)]
    speak(f'Playing {mov}')
    os.startfile(movies_dir+mov)

import cv2
def hackmyphone(ip_address):
    capture=cv2.VideoCapture(f"http:{ip_address}:8080/video")
    while True:
        success,frame=capture.read()

        cv2.imshow('Phone Camera',frame)
        if cv2.waitKey(1)==ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

hackmyphone('192.168.43.159')