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
pet_name = StoryNode("name")
pet_breed = StoryNode("breed")
age  = StoryNode("age")
favorite_toy = StoryNode("toy")
#physical char.
color = StoryNode("color")
big_or_small  = StoryNode("size")
#other char.
sound = StoryNode("sound")
mess = StoryNode("mess")
sleep = StoryNode("sleep")
#food
food = StoryNode("food")
treat = StoryNode("treat")
#social
siblings = StoryNode("siblings")
other_pets = StoryNode("other pets")
temperment = StoryNode("temperment")
vet = StoryNode("vet")
#doing things
walk = StoryNode("walks")
tricks = StoryNode("tricks")

done = StoryNode("done", "I loved talking to you. But I have to go. Goodbye!")

"""ADD CHILDREN"""

have_pets.addChild(kinds_of_pets).addChild(done)
#.addChild(color).addChild(sound).addChild(food).addChild(siblings).addChild(walk)
#.addChild(dream_pets)
kinds_of_pets.addChild(pet_name).addChild(done)
pet_name.addChild(pet_breed).addChild(done)
pet_breed.addChild(age).addChild(done)
age.addChild(favorite_toy).addChild(done)
color.addChild(big_or_small).addChild(done)
sound.addChild(mess).addChild(done)
mess.addChild(sleep).addChild(done)
food.addChild(treat).addChild(done)
siblings.addChild(other_pets).addChild(done)
other_pets.addChild(temperment).addChild(done)
temperment.addChild(vet).addChild(done)
walk.addChild(tricks).addChild(done)

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
age.setActivity(Activity(age_act))
favorite_toy.setActivity(Activity(toy_act))
color.setActivity(Activity(color_act))
big_or_small.setActivity(Activity(size_act))
sound.setActivity(Activity(sound_act))
mess.setActivity(Activity(mess_act))
sleep.setActivity(Activity(sleep_act))
food.setActivity(Activity(food_act))
treat.setActivity(Activity(treat_act))
siblings.setActivity(Activity(sibs_act))
other_pets.setActivity(Activity(friends_act))
temperment.setActivity(Activity(temperment_act))
vet.setActivity(Activity(vet_act))
walk.setActivity(Activity(walk_act))
tricks.setActivity(Activity(tricks_act))
done.setActivity(Activity(done_act))


pet_story_line = [have_pets, kinds_of_pets, pet_name, pet_breed, age, favorite_toy,
                        color, big_or_small, sound, mess, sleep, food, treat,
                        siblings, other_pets, temperment, vet, walk, tricks]

