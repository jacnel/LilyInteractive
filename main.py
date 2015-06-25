from story import Story
from story_node import StoryNode
from player import Player
from activity import Activity
from theater_acts import *
from zoo_acts import *
from text_to_speech import *
from speech_recog import *
import movie_story
import zoo_story

story_dict = {}
story_dict["Movie"] = movie_story.movie_story_line
story_dict["Zoo"] = zoo_story.zoo_story_line

def getStory():
    speak("Which story would you like to play?")
    for story in story_dict.keys():
        speak(story)
    while True:
        s = getInputString()
        for story in story_dict.keys():
            if s.lower() == story.lower():
                return story_dict[story]
        speak("Sorry, we don't have that story right now.")
        speak("Please try another.")

def runStory():
    #create story from nodes and player 
    story_line = getStory()
    player = Player(story_line)
    story = Story(player, story_line)
    #run through the story
    story.walk(player)

runStory()
