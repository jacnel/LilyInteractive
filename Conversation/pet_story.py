from story import Story
from story_node import StoryNode
from player import Player
from activity import Activity
from text_to_speech import *

"""NODES = Q'S"""

pets = StoryNode("top node", "top node")
have_pets = StoryNode("have pets","Do you have any pets?")

dream_pet = StoryNode("dream pet", "What would be your dream pet to have?")

#basic info
kinds_of_pets = StoryNode("kinds of pets", "What kinds of pets do you have?")
pet_name = StoryNode("What are your pets' names?")
pet_breed = StoryNode("breed", "What breed is your pet?")
age  = StoryNode("age", "How old is your pet?")
favorite_toy = StoryNode("toy", "What is your pet's favorite toy or game?")
#physical char.
color = StoryNode("color", "What color is your pet?")
legs  = StoryNode("legs", "How many legs does your pet have?")
big_or_small  = StoryNode("size", "Is your pet big or small?")
tail = StoryNode("tail", "Does your pet have a tail?")
ears = StoryNode("ears", "Does your pet have ears?")
#other char.
sound = StoryNode("sound", "What sounds does your pet make?")
shed = StoryNode("shed", "Does your pet shed?")
mess = StoryNode("mess", "Is your pet messy?")
sleep = StoryNode("sleep", "Where does your pet usually sleep?")
#food
food = StoryNode("food", "Who in your family feeds your pet?")
treat = StoryNode("treat", "What is your pet's favorite treat?")
#social
siblings = StoryNode("siblings", "Does your pet have any siblings?")
other_pets = StoryNode("other pets", "Does your pet have animal friends?")
temperment = StoryNode("temperment", "Does your pet like strangers?")
vet = StoryNode("vet", "Does your pet like going to the vet?")
#doing things
walk = StoryNode("walks", "Do you take your pet on walks?")
tricks = StoryNode("tricks", "Can your pet do any tricks?")

"""ADD CHILDREN"""

pets.addChild(have_pets).addChild(dream_pet)
have_pets.addChild(kinds_of_pets).addChild(dream_pet).addChild(color).addChild(sound).addChild(food).addChild(siblings).addChild(walk)
kinds_of_pets.addChild(pet_name)
pet_name.addChild(pet_breed)
pet_breed.addChild(age)
age.addChild(favorite_toy)
color.addChild(legs)
legs.addChild(big_or_small)
big_or_small.addChild(tail)
tail.addChild(ears)
sound.addChild(shed)
shed.addChild(mess)
mess.addChild(sleep)
food.addChild(treat)
siblings.addChild(other_pets)
other_pets.addChild(temperment)
temperment.addChild(vet)
walk.addChild(tricks)

#not sure about this!
favorite_toy.addChild(have_pets)
ears.addChild(have_pets)
sleep.addChild(have_pets)
treat.addChild(have_pets)
vet.addChild(have_pets)
tricks.addChild(have_pets)

"""ACTIVITIES"""



pet_story_line = [pets, have_pets, dream_pet, kinds_of_pets, pet_name, pet_breed, age, favorite_toy,
                        color, legs, big_or_small, tail, ears, sound, shed, mess, sleep, food, treat,
                        siblings, other_pets, temperment, vet, walk, tricks]
