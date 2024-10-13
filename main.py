class Peacock:
    colour = "Blue"
    def __init__ (self, name, age):
        self.name = name
        self.age = age

obj1 = Peacock("Pedro", 6)
obj2 = Peacock("Estrovet", 19)

print("The name of the first peacock is", obj1.name)
print("The colour of Pedro is: ", obj1.colour)
print("The age of the Pedro is: ", obj1.age)

print("The name of the second peacock is", obj2.name)
print("The colour of Estrovet is: ", obj2.colour)
print("The age of the Estrovet is: ", obj2.age)
