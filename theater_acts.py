from player import Player
#import ctypes
#import time
#lib = ctypes.CDLL('FakeInputWin')
from speech_recog import *
from text_to_speech import *

def theaterActivity():
    speak("You have arrived at the movies")


def boxOfficeActivity(player, movies):
    speak("Which movie would you like to watch?")
    
    for i in range(len(movies[0])):
       speak(str(movies[0][i]))
    movieChoice = getInputString()
    while not inList(movies, movieChoice):
        speak("Sorry, we don't have that movie. Pick another.")
        for i in range(len(movies[0])):
            speak(str(movies[0][i]))
        movieChoice = getInputString()
    player.completed["ticket"] = movieChoice

def concessionsActivity(player, menu):
    done = False
    menu[0].append("Done")
    while not done:
        speak("What can I get for you?")
        for i in range(len(menu[0])):
            speak(str(menu[0][i]))
        menuChoice = getInputString()
        while not inList(menu, menuChoice):
            speak("Sorry, we don't have that. Pick another.")
            menuChoice = getInputString()
        if menuChoice.lower() == "done":
            done = True
    speak("Here you go. Thank you.")

def inList(lst, s):
    for x in lst[0]:
        if s.lower() == x.lower():
            return True
    return False


"""def speak(prompt, x):
    print prompt
    lib.typeInBaldi(prompt)
    time.sleep(x)"""













        
