from player import Player
from speech_recog import *
from text_to_speech import *
from story_node import StoryNode
import random
import animal

#acts must pass player as a parameter

flag = True
pet_name = ""
pet = None

def have_pets_act(player):
    current = player.location
    speak("Hi " + player.name)
    speak (current.description)
    s = getInputString()
    if s.lower() == "no":
        return "done"
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

def kinds_act(player):
    global pet
    current = player.location
    speak(current.description)
    s = getInputString()
    pet = animal.Animal(s.split())
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

def name_act(player):
    global pet_name
    current = player.location
    speak("What is your " + pet.type + "'s name?")
    s = getInputString()
    pet_name = s
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

def breed_act(player):
    current = player.location
    speak("What breed is " + pet_name + "?")
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

def age_act(player):
    current = player.location
    speak("How old is your " + pet.type + "?")
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

def toy_act(player):
    current = player.location
    speak("What is your " + pet.type + "'s favorite toy or game?")
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

def color_act(player):
    current = player.location
    speak("What color " + pet.bc_plural+ " your " + pet.type + "'s " + pet.body_covering + "?")
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

def size_act(player):
    current = player.location
    speak("Is " + pet_name + " big or small?")
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

def sound_act(player):
    current = player.location
    speak("What sound does " + pet_name + " make?")
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

def mess_act(player):
    current = player.location
    speak("Is your " + pet.type + " messy?")
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

def sleep_act(player):
    current = player.location
    speak("Where does " + pet_name + " usually sleep?")
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

def food_act(player):
    current = player.location
    speak("Who in your family feeds your " + pet.type + " its " + pet.eats +"?")
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

def treat_act(player):
    current = player.location
    speak("What is " + pet_name + "'s favorite treat?")
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

def sibs_act(player):
    current = player.location
    speak("Does " + pet_name + " have any siblings?")
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

def friends_act(player):
    current = player.location
    speak("Does " + pet_name + " have animal friends?")
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

def temperment_act(player):
    current = player.location
    speak("Does your " + pet.type + " like strangers?")
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

def vet_act(player):
    current = player.location
    speak("Does " + pet_name + " like going to the vet?")
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

def walk_act(player):
    current = player.location
    speak("Do you take " + pet_name + " on walks?")
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

def tricks_act(player):
    current = player.location
    speak("Can " + pet_name + " do any tricks?")
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
