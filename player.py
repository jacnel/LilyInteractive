class Player:
    def __init__(self, a_name, a_age, list_of_StoryNodes):
        self.name = a_name
        self.age = a_age
        #requires that first StorNode in list is start node
        self.location = list_of_StoryNodes[0]
        self.completed = {}
        
        for node in list_of_StoryNodes:
            self.completed[node.name] = False

    def getLoc(self):
        return self.location
 
    def addCompleted(self, current):
        self.completed.append(current.name)
