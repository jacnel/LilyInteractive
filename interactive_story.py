from story import Story
from story_node import StoryNode
from player import Player
from activity import Activity
from theater_acts import *
from zoo_acts import *
from pet_acts import *
from _vault_acts import *
from text_to_speech import *
from speech_recog import *
import movie_story
import zoo_story
import pet_story
import _vault_story
import threading
import avatar_player
import time

#all story titles must be one word

story_dict = {}
story_dict["Movie"] = movie_story.movie_story_line
story_dict["Zoo"] = zoo_story.zoo_story_line
story_dict["Pet"] = pet_story.pet_story_line
story_dict["Vault"] = _vault_story.vault_story_line

targets_syn = []
for name in story_dict.keys():
    targets_syn.append(stemmer.stem(name))
print "keys are:"
print story_dict.keys()
print "syns are:"
print targets_syn

def getStory():
    speak("Which story would you like to play?")
    for story in story_dict.keys():
        speak(story)
    while True:
        s = getInputString()
        story = get_target(s, story_dict.keys(), targets_syn)
        while story == None:
            speak("Sorry, we don't have that story right now.")
            speak("Please try another.")
            for story in story_dict.keys():
                speak(story)
            s = getInputString()
            story = get_target(s, story_dict.keys(), targets_syn)
        return story_dict[story]

def get_target(s, targets, targets_syn):        #this method looks for a one word target in user's speech
    #check if user says exactly the node's name
    for t in targets:
        if s.lower() == t.lower():
            return t
    
    s = s.lower().split()
    temp = []
    for i in s:
        temp.append(stemmer.stem(i))
    s = temp
    print "s:"
    print s
    for word in s:
        count = 0
        if word in targets_syn:
            print word
            print "found match"
            print targets[count]
            return targets[count]
        count += 1
    return None

   
def runStory():
        #play avatar
	t = threading.Thread(target = avatar_player.run_avatar)
	t.daemon = True
	t.start()
	time.sleep(2)
	#create story from nodes and player 
	story_line = getStory()
	player = Player(story_line)
	story = Story(player, story_line) 
	#run through the story
	story.walk(player)

runStory()

