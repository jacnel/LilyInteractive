from player import Player
from speech_recog import *
from text_to_speech import *
import webbrowser
import random
import time
from Tkinter import *
from PIL import Image, ImageTk


#activities must return None or the name of the next node or "quit"

def entranceAct(player):
    speak("Hi " + player.name + ". Welcome to the San Deigo Zoo!")
    speak("How many tickets would you like?")
    s = int(getInputString())
    #cost = str(15*s)
    #speak("That will be $" + cost)
    #time.sleep(1)
    x = random.random()
    if x > 0.9:
        speak("Oh no! You forgot your wallet!")
        speak("The End.")
        return "quit"
    speak("Ok, here's your map.")
    speak("Have a fun day!")
    speak("Say leave at any time to leave the zoo.")
    speak("Where should we start?")
    speak("We can go to the monkeys or the elephants.")
    return None
    
def parking_lotAct(player):
    speak("You've reached the parking lot.")
    x = random.random()
    if x > 0.5:
        speak("Oh no! Some monkeys escaped.")
        speak("They have gotten into your car!")
        displayImage("ZooGifs/monkey_steals_wheel_cover.gif")
        speak("Let's get out of here. The End.")
        return "quit"
    speak("Time to go home. The End.")
    return "quit"

def monkeyAct(player):
    speak("This is the monkey exhibit. Do you want to stop here?")
    s = getInputString()
    if s.lower() == "yes":
       displayImage("ZooGifs/monkey_falling.gif")
    speak("Where to now?")
    speak("Elephants, lions, or penguins?")
    return None

def elephantAct(player):
    speak("We're at the elephants. Should we stop?")
    s = getInputString()
    if s.lower() == "yes":
        displayImage("ZooGifs/GIF-Elephant-painting.gif")
    speak("Where to now?")
    speak("Lions, monkeys, or tigers?")
    return None

def lionAct(player):
    speak("We're at the lions. Should we stop?")
    s = getInputString()
    if s.lower() == "yes":
        displayImage("ZooGifs/lion_tries_to_grab_baby.gif")
    speak("Where to now?")
    speak("Monkeys, elephants, penguins, tigers?")
    return None
    
def penguinAct(player):
    speak("Here are the penguins. Want to stop?")
    s = getInputString()
    if s.lower() == "yes":
        displayImage("ZooGifs/penguin.gif")
    x = random.random()
    if x > 0.25:
        speak("Great timing. They are feeding the penguins.")
        speak("Want to watch?")
        s = getInputString()
        if s.lower() == "yes":
            displayImage("ZooGifs/penguin_feeding.gif")
    speak("Where to now?")
    speak("Monkeys, lions, or otters?")
    return None

def tigerAct(player):
    speak("Oooh tigers. Want to stop?")
    s = getInputString()
    if s.lower() == "yes":
        displayImage("ZooGifs/tiger_and_bird.gif")
    x = random.random()
    if x > 0.75:
        speak("There are baby tigers too!")
        speak("Want to look?")
        s = getInputString()
        if s.lower() == "yes":
            displayImage("ZooGifs/baby_tiger.gif")
    speak("Where to now?")
    speak("Elephants, lions, or otters?")
    return None

def otterAct(player):
    speak("Here are the otters. Want to stop?")
    s = getInputString()
    if s.lower() == "yes":
        displayImage("ZooGifs/otter_basketball.gif")
        x = random.random()
        if x > 0.5:
            speak("Look! There is a special white shark exhibit!")
            speak("Do you want to stop?")
            s = getInputString()
            if s.lower() == "yes":
                displayImage("ZooGifs/white_shark_feeding.gif")
    speak("Where to now?")
    speak("Penguins, tigers, or pandas?")
    return None

def pandaAct(player):
    speak("Here are the pandas. Want to stop?")
    s = getInputString()
    if s.lower() == "yes":
        displayImage("ZooGifs/pandas_falling_down_slide.gif")
    speak("This is a dead end.")
    speak("To go anywhere else, we have to go back to the otters.")
    speak("Or we can leave from here.")
    return None

def displayImage(im):
    root = Tk()
    photo = PhotoImage(file = im)
    w = Label(parent,image = photo)
    w.photo = photo
    w.pack()

displayImage("ZooGifs/white_shark_feeding.gif")
