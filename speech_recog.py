import speech_recognition as sr
from text_to_speech import *

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:                 # use the default microphone as the audio source
        audio = r.adjust_for_ambient_noise(source, duration = 1)
        r.energy_threshold = 1000
        audio = r.listen(source)                    # listen for the first phrase and extract it into audio dataprint "heard"
    try:
        return "" + r.recognize(audio)   # recognize speech using Google Speech Recognition
    except LookupError:                            # speech is unintelligible
        speak("Sorry, I didn't hear that. Please say it again.")

def getInputString():
    s = voice_input()
    while( s == None):
        s = voice_input()
    print(s)
    return str(s)


