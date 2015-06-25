'''This class represents a distinct moment in an interactive story.
It will have fields for a name, description, necessary conditions to be
available, and child story events. Additionally, activities are attributed to
each node and allow for more interactivity between user and story'''
from activity import Activity

class StoryNode:
    # only necessary parameters are name and description
    def __init__(self, a_name, a_description, the_prereqs = None, the_children = None, an_activity = None):
        self.name = str(a_name)
        self.description = a_description
        # add prerequisites for story node to be valid
        self.prereqs = []
        if the_prereqs != None:
            for req in the_prereqs:
                self.prereqs.append(req)
        # add children StoryNodes to this node, possible edges in graph
        self.children = []
        if the_children != None:
            for child in the_children:
                if isinstance(child, StoryNode):
                    self.children.append(child)
        # add activities to the node to be completed
        self.activity = None
        if an_activity != None:
            self.activity = an_activity

    '''def getChild(self, child):
        for each_child in self.children:
            if each_child == child:
                return each_child
            else:
                print "No matching children were found"
                return '''
	# adds new children to a node, adding them to children list
    def addChild(self, child):
        if isinstance(child, StoryNode):
            self.children.append(child)
        else:
            print "child is not a StoryNode"
        return self

	# adds new activities to a node
    def setActivity(self, activ): # an activity is simply a wrapper class for a user defined function (allows for customization of activities)
        if isinstance(activ, Activity):
            self.activity = activ
        else:
            print "not an Activity"
        return self


