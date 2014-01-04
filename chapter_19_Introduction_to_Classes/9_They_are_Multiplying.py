class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("CHN", 5000)
sloth = Animal("JPN", 3000)
ocelot = Animal("USA", 300)

print hippo.health
print sloth.health
print ocelot.health