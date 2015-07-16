from text_to_speech import *
from speech_recog import *

yes_syns = [['yes', 'yup', 'yeah', 'yea', 'indeed', 'sure']]

class Player:
    def __init__(self, list_of_StoryNodes):
        #requires that first StorNode in list is start node
        self.location = list_of_StoryNodes[0]
        self.completed = {}

        self.name = self.setName()

        #put all nodes in story in dictionary as not completed
        for node in list_of_StoryNodes:
            self.completed[node.name] = False

    def getLoc(self):
        return self.location
 
    def addCompleted(self, current):
        self.completed.append(current.name)

    def setName(self):
        return "Elise"
        do:
            speak("What is your name?")
            s = getInputString()
            speak("Is your name " + s + "?")
            yes = getInputString()
        while (get_target(yes, ['yes'], yes_syns) != 'yes')
        return s

    def get_target(self, s, targets, targets_syn):
        #check if user says exactly the node's name
        for t in targets:
            if s.lower() == t.lower():
                return t
        
        s = s.lower().split()
        for word in s:
            for t in targets_syn:
                if word in t:
                    return targets[targets_syn.index(t)]
        return None
