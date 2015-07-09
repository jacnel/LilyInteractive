from player import Player
from speech_recog import *
from text_to_speech import *
import webbrowser

#activities must return None or the name of the next node or "quit"

def theaterActivity(player):
    speak("Hello! Welcome to the Lehigh Valley Movie Theater")
    speak("You can go to the box office and get your ticket")
    speak("Or you can go to the concessions for some snacks.")
    speak("Where would you like to go, " + player.name + "?")

    return None

def boxOfficeActivity(player, box_args):
    speak("Welcome to the box office")
    speak("Which movie would you like to watch?")
    for i in range(len(box_args[0])):
       speak(str(box_args[0][i]))
    movieChoice = getInputString()
    while not inList(box_args[0], movieChoice):
        speak("Sorry, we don't have that movie. Pick another.")
        for i in range(len(box_args[0])):
            speak(str(box_args[0][i]))
        movieChoice = getInputString()
    player.completed["ticket"] = movieChoice
    speak("Here's your ticket. Enjoy the show.")
    speak("Would you like to go to the concessions?")
    speak("Or would you like to go to the ticket checker?")

    return None

def concessionsActivity(player, menu):
    done = False
    speak("What can I get for you?")
    while not done:
        for i in range(len(menu[0])):
            if not menu[0][i].lower() in player.completed.keys():
                speak(str(menu[0][i]))
        menuChoice = getInputString()
        while not inList(menu[0], menuChoice):
            speak("Sorry, we don't have that. Pick another.")
            menuChoice = getInputString()
        if menuChoice.lower() == "done":
            done = True
        else:
            player.completed[menuChoice] = True
            speak("Can I get anything else for you?")
    speak("Thank you. Next please!")

    speak("If you do not have your ticket yet, go to the box office")
    speak("Otherwise you can go to the ticket checker.")

    return None

def ticketCheckerActivity(player):
    speak("Hello, ticket please")
    if player.completed["ticket"].lower() == "inside out":
        speak("Inside Out is in theater 3A, enjoy the show!")
    if player.completed["ticket"].lower() == "tomorrow land":
        speak("Tomorrowland is in theater 1D, enjoy your movie!")
    if player.completed["ticket"].lower() == "minions":
        speak("Minions is in theater 3B, enjoy the show!")
    if player.completed["ticket"].lower() == "home":
        speak("Home is in theater 1A, enjoy your movie!")
    speak("Say movie to sit down and watch.")

    return None

def movieActivity(player):
    speak("Please power off your cellular devices.")
    speak("Sit back, relax and enjoy the show.")
    if player.completed["ticket"].lower() == "inside out":
        webbrowser.open("https://www.youtube.com/watch?v=_MC3XuMvsDI", new=1)
    if player.completed["ticket"].lower() == "tomorrow land":
        webbrowser.open("https://www.youtube.com/watch?v=1k59gXTWf-A", new=1)
    if player.completed["ticket"].lower() == "minions":
        webbrowser.open("https://www.youtube.com/watch?v=eisKxhjBnZ0", new=1)
    if player.completed["ticket"].lower() == "home":
        webbrowser.open("https://www.youtube.com/watch?v=MyqZf8LiWvM", new=1)

    return "quit"

def inList(lst, s):
    for x in lst:
        if s.lower() == x.lower():
            return True
    return False














        
