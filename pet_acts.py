from player import Player
from speech_recog import *
from text_to_speech import *
from story_node import StoryNode
import random

#acts must pass player as a parameter

flag = True
pet_name = ""
pet_type = []

def have_pets_act(player):
    current = player.location
    speak("Hi, " + player.name)
    speak (current.description)
    s = getInputString()
    if s.lower() == "no":
        return "done"
    return current.children[0].name

def kinds_act(player):
    global pet_type
    current = player.location
    speak(current.description)
    s = getInputString()
    pet_type = s.split()
    return current.children[0].name

def name_act(player):
    global pet_name
    current = player.location
    speak(current.description)
    s = getInputString()
    pet_name = s
    return current.children[0].name

def breed_act(player):
    current = player.location
    speak("What breed is " + pet_name + "?")
    s = getInputString()
    return current.children[0].name

def color_act(player):
    current = player.location
    if "dog" in pet_type:
        speak("What color is your dog's fur?")
    elif "cat" in pet_type:
        speak("What color is your cat's fur?")
    elif "fish" in pet_type:
        speak("What color are your fish's scales?")
    elif "bird" in pet_type:
        speak("What color are your bird's feathers?")
    elif "lizard" in pet_type:
        speak("What color is your lizard's skin?")
    else:
        speak("What color is your pet?")
    s = getInputString()
    return current.children[0].name

def pet_act(player):
    current = player.location
    speak(current.description)
    s = getInputString()
    if len(current.children) == 1:
        return current.children[0].name
    num_childs = len(current.children)
    x = random.randint(0,num_childs-2)
    while inList(player.completed, current.children[x]):
        if not flag:
            x = random.randint(0,num_childs-1)
        else:       
            return "done"
    return current.children[x].name

def inList(dct, s):
    global flag
    flag = True
    inLst = False
    for x in dct.keys():
        if dct[x] == False:
            flag = False
        if s.name.lower() == x.lower() and dct[x] == True:
            inLst = True

    return inLst

def done_act(player):
    speak (player.location.description)
    return "quit"
