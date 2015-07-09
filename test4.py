from story import Story
from story_node import StoryNode
from player import Player
from activity import Activity
from zoo_acts import *
import random
from text_to_speech import *

#nodes
entrance = StoryNode("entrance")
parking_lot = StoryNode("leave")
monkeys = StoryNode("monkeys")
elephants = StoryNode("elephants")
lions = StoryNode("lions")
tigers = StoryNode("tigers")
penguins = StoryNode("penguins")
otters = StoryNode("otters")
pandas = StoryNode("pandas")

exhibits = [monkeys, elephants, lions, tigers, penguins, otters, pandas]
current_exhibits = []

#pick one of the exhibits
for x in range(4):
    rand_num = random.randint(1, len(exhibits))
    current_exhibits.append(exhibits[x])
    exhibits.remove(exhibits[x])
print current_exhibits
print exhibits


#add children
entrance.addChild(parking_lot).addChild(monkeys).addChild(elephants)
monkeys.addChild(elephants).addChild(lions).addChild(penguins).addChild(parking_lot)
elephants.addChild(monkeys).addChild(lions).addChild(tigers).addChild(parking_lot)
lions.addChild(monkeys).addChild(elephants).addChild(penguins).addChild(tigers).addChild(parking_lot)
penguins.addChild(lions).addChild(monkeys).addChild(otters).addChild(parking_lot)
tigers.addChild(elephants).addChild(lions).addChild(otters).addChild(parking_lot)
otters.addChild(tigers).addChild(penguins).addChild(pandas).addChild(parking_lot)
pandas.addChild(otters).addChild(parking_lot)

#set activities

entrance.setActivity(Activity(entranceAct))
parking_lot.setActivity(Activity(parking_lotAct))
monkeys.setActivity(Activity(monkeyAct))
elephants.setActivity(Activity(elephantAct))
lions.setActivity(Activity(lionAct))
tigers.setActivity(Activity(tigerAct))
penguins.setActivity(Activity(penguinAct))
otters.setActivity(Activity(otterAct))
pandas.setActivity(Activity(pandaAct))

zoo_story_line = [entrance, monkeys, elephants, lions, tigers, penguins, otters, pandas, parking_lot]
