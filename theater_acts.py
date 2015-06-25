from player import Player
#import ctypes
#import time
#lib = ctypes.CDLL('FakeInputWin')
from speech_recog import *
from text_to_speech import *

import webbrowser

def theaterActivity(player):
    speak("Hello! Welcome to the Lehigh Valley Movie Theater")
    speak("You can go to the box office and get your ticket")
    speak("or you can go to the concessions for some snacks")
    speak("Where would you like to go, " + player.name + "?")


def boxOfficeActivity(player, box_args):
    speak("Welcome to the box office")
    speak("Which movie would you like to watch?")
    for i in range(len(box_args[0])):
       speak(str(box_args[0][i]))
       speak(str(box_args[1][i]))
    movieChoice = getInputString()
    while not inList(box_args[0], movieChoice):
        speak("Sorry, we don't have that movie. Pick another.")
        for i in range(len(box_args[0])):
            speak(str(box_args[0][i]))
        movieChoice = getInputString()
    player.completed["ticket"] = movieChoice
    speak("Would you like to go to the concessions?")
    speak("or would you like to go to the ticket checker")
    

def concessionsActivity(player, menu):
    done = False
    speak("What can I get for you?")
    while not done:
        for i in range(len(menu[0])):
            if not menu[0][i].lower() in player.completed.keys():
                speak(str(menu[0][i]))
        menuChoice = getInputString()
        while not inList(menu, menuChoice):
            speak("Sorry, we don't have that. Pick another.")
            menuChoice = getInputString()
        if menuChoice.lower() == "done":
            done = True
        else:
            player.completed[menuChoice] = True
            speak("Can I get anything else for you?")
    speak("Enjoy your movie. Next please!")

    speak("If you do not have your ticket yet, go to the box office")
    speak("Otherwise you can go to the ticket checker")

def ticketCheckerActivity(player):
    speak("Hello, ticket please")
    if player.completed["ticket"].lower() == "jurassic world":
        speak("Jurassic world is in theater 3A, enjoy the show!")
    if player.completed["ticket"].lower() == "mad max":
        speak("Mad Max is in theater 1D, enjoy your movie!")
    speak("say movie to sit down and watch")

def movieActivity(player):
    speak("please power off you cellular devices")
    speak("sit back, relax and enjoy the show")
    if player.completed["ticket"].lower() == "jurassic world":
        webbrowser.open("https://www.youtube.com/watch?v=RFinNxS5KN4", new=1)
    if player.completed["ticket"].lower() == "mad max":
        webbrowser.open("https://www.youtube.com/watch?v=hEJnMQG9ev8", new=1)

def inList(lst, s):
    for x in lst[0]:
        if s.lower() == x.lower():
            return True
    return False

"""def speak(prompt, x):
    print prompt
    lib.typeInBaldi(prompt)
    time.sleep(x)"""













        
