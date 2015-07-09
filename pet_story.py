from story import Story
from story_node import StoryNode
from player import Player
from activity import Activity
from text_to_speech import *
from pet_acts import *

"""NODES = Q'S"""

have_pets = StoryNode("have pets","Do you have any pets?")

#dream_pet = StoryNode("dream pet", "What would be your dream pet to have?")

#basic info
kinds_of_pets = StoryNode("kinds of pets", "Tell me about a pet of yours. What kind of pet is it?")
pet_name = StoryNode("name","What is your pet's name?")
pet_breed = StoryNode("breed")
age  = StoryNode("age", "How old is your pet?")
favorite_toy = StoryNode("toy", "What is your pet's favorite toy or game?")
#physical char.
color = StoryNode("color")
big_or_small  = StoryNode("size", "Is your pet big or small?")
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

done = StoryNode("done", "I loved talking to you. But I have to go. Goodbye!")

"""ADD CHILDREN"""

have_pets.addChild(kinds_of_pets).addChild(done)
#.addChild(color).addChild(sound).addChild(food).addChild(siblings).addChild(walk)
#.addChild(dream_pets)
kinds_of_pets.addChild(pet_name)
pet_name.addChild(pet_breed)
pet_breed.addChild(age)
age.addChild(favorite_toy)
color.addChild(big_or_small)
sound.addChild(shed)
shed.addChild(mess)
mess.addChild(sleep)
food.addChild(treat)
siblings.addChild(other_pets)
other_pets.addChild(temperment)
temperment.addChild(vet)
walk.addChild(tricks)

#not sure about this!
#dream_pet.addChild(kinds_of_pets).addChild(color).addChild(sound).addChild(food).addChild(siblings).addChild(walk).addChild(done)
favorite_toy.addChild(color).addChild(sound).addChild(food).addChild(siblings).addChild(walk).addChild(done)
big_or_small.addChild(sound).addChild(food).addChild(siblings).addChild(walk).addChild(done)
sleep.addChild(color).addChild(food).addChild(siblings).addChild(walk).addChild(done)
treat.addChild(color).addChild(sound).addChild(siblings).addChild(walk).addChild(done)
vet.addChild(color).addChild(sound).addChild(food).addChild(walk).addChild(done)
tricks.addChild(color).addChild(sound).addChild(food).addChild(siblings).addChild(done)

"""ACTIVITIES"""
have_pets.setActivity(Activity(have_pets_act)) 
#dream_pet.setActivity(Activity(pet_act))
kinds_of_pets.setActivity(Activity(kinds_act))
pet_name.setActivity(Activity(name_act))
pet_breed.setActivity(Activity(breed_act))
age.setActivity(Activity(pet_act))
favorite_toy.setActivity(Activity(pet_act))
color.setActivity(Activity(pet_act))
big_or_small.setActivity(Activity(pet_act))
sound.setActivity(Activity(pet_act))
shed.setActivity(Activity(pet_act))
mess.setActivity(Activity(pet_act))
sleep.setActivity(Activity(pet_act))
food.setActivity(Activity(pet_act))
treat.setActivity(Activity(pet_act))
siblings.setActivity(Activity(pet_act))
other_pets.setActivity(Activity(pet_act))
temperment.setActivity(Activity(pet_act))
vet.setActivity(Activity(pet_act))
walk.setActivity(Activity(pet_act))
tricks.setActivity(Activity(pet_act))
done.setActivity(Activity(done_act))


pet_story_line = [have_pets, kinds_of_pets, pet_name, pet_breed, age, favorite_toy,
                        color, big_or_small, sound, shed, mess, sleep, food, treat,
                        siblings, other_pets, temperment, vet, walk, tricks]

