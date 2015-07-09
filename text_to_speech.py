import pyttsx
import run_gif2
import threading
import win32con, win32api



engine = pyttsx.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + .99)
#engine.setProperty('rate', rate - 70)
engine.setProperty('voice', voices[1].id)


import ctypes
import time
import math

#lib = ctypes.CDLL('FakeInputWin')

def speak(string):
        engine.say(string)
        print string
        click(100,100)
        engine.runAndWait()
        click(100,100)

def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        

#lib.typeInBaldi(string)
#time.sleep(2*math.log10(len(string)) + 1)"""


