import pyttsx
import win32con, win32api


'''This file handles the text to speech aspect of the interactive story using the pyttsx module to 
produce the speech. Additionally, we use the win32api module for python, which encapsulates the Windows win32api, allowing
us to send a click to our avatar. Each click changes the current avatar animation being run, simulating a talking or idle state. '''

engine = pyttsx.init()
#get functions return current state of speech engine
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
#set the speaking volume
engine.setProperty('volume', volume + .99)
#set the speaking rate
#engine.setProperty('rate', rate - 70)
#set the voice to one of three
engine.setProperty('voice', voices[1].id)


import ctypes
import time
import math

#lib = ctypes.CDLL('FakeInputWin')

def speak(string):
        engine.say(string)
        click(100,100)
        engine.runAndWait()
        click(100,100)
        print string


def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        
#IN THE EVENT BALDISYNC IS USED REPLACE SPEAK WITH BELOW CODE
#lib.typeInBaldi(string)
#time.sleep(2*math.log10(len(string)) + 1)


