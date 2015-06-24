from story import Story
from story_node import StoryNode
from player import Player
from activity import Activity
from theater_acts import *

from text_to_speech import *

#import ctypes
#lib = ctypes.CDLL('FakeInputWin')

#create each node in the story
theater = StoryNode("theater", "welcome to the theater!")
box_office = StoryNode("box office", "choose the movie you would like to watch and buy your ticket here!")
concessions = StoryNode("concessions", "if you would like to get some popcorn or something to drink here is place")
ticket_checker = StoryNode("ticket checker", "you must have your ticket checked before you can enter the movie")
movie = StoryNode("movie", "have a seat and enjoy the show!")

#add connections between nodes
theater.addChild(box_office).addChild(concessions)
concessions.addChild(box_office).addChild(ticket_checker)
box_office.addChild(concessions).addChild(ticket_checker)
ticket_checker.addChild(movie)

#add prerequisites (something that must be completed before moving to this node)
ticket_checker.prereqs.append("ticket")

#create activities and add them to their corresponding nodes
movies = ["Jurassic World", "Mad Max"]
menu = ["Soda", "Popcorn", "Candy"]

t = Activity(theaterActivity)
#movies and menu are lists of options for the activity
#currently activities are simply choosing between options
b = Activity(boxOfficeActivity, movies)
c = Activity(concessionsActivity, menu)
  
theater.addActivity(t)
box_office.addActivity(b)
concessions.addActivity(c)

def runStory():
    #create story from nodes and player 
    story_line = [theater, concessions, box_office, ticket_checker, movie]
    elise = Player("Elise", 21, story_line)
    story = Story(elise, story_line)

    #run through the story
    story.walk(elise)
    speak("enjoy the show!")

    
    
