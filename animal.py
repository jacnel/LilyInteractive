class Animal(object):
    def __init__(self, pet_type):
        if "dog" in pet_type:
            self.type = "dog"
            self.feet = "paws"
            self.mouth = "mouth"
            self.body_covering = "fur"
            self.bc_plural = "is"
            self.tail = True
            self.eats = "dog food"
            
        elif "cat" in pet_type:
            self.type = "cat"
            self.feet = "paws"
            self.mouth = "mouth"
            self.body_covering = "fur"
            self.bc_plural = "is"
            self.tail = True
            self.eats = "cat food"
        elif "fish" in pet_type:
            self.type = "fish"
            self.feet = "fins"
            self.mouth = "mouth"
            self.body_covering = "scales"
            self.bc_plural = "are"
            self.tail = False
            self.eats = "fish food"
        elif "bird" in pet_type:
            self.type = "bird"
            self.feet = "claws"
            self.mouth = "beak"
            self.body_covering = "feathers"
            self.bc_plural = "are"
            self.tail = False
            self.eats = "seeds"
        elif "lizard" in pet_type:
            self.type = "lizard"
            self.feet = "feet"
            self.mouth = "mouth"
            self.body_covering = "skin"
            self.bc_plural = "is"
            self.tail = True
            self.eats = "cricekts"
        else:
            self.type = "pet"
            self.feet = "feet"
            self.mouth = "mouth"
            self.body_covering = "body"
            self.bc_plural = "is"
            self.tail = None
            self.eats = "pet food"
