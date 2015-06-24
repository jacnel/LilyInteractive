"""import pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + .99)
#engine.setProperty('rate', rate - 70)
engine.setProperty('voice', voices[1].id)
"""

import ctypes
import time
import math

lib = ctypes.CDLL('FakeInputWin')

def speak(string):
	
	lib.typeInBaldi(string)
	time.sleep(2*math.log10(len(string)) + 1)
	#engine.say(string)
	print string
	#engine.runAndWait()

