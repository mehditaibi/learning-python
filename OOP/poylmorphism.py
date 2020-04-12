# An object can take many (poly) forms (morph)
# 1 - The same class method works in a similar way for different classes
# e.g.
# Cat.speak() # meow
# Dog.speak() # woof
# Human.speak() # yo
# 2 - The same operation works for different kinds of objects


class Animal():
    def speak(self):
        raise NotImplementedError("Subcass needs to implement this method")


def Dog(Animal):
    def speak(self):
        return "woof"


def Cat(Animal):
    def speak(self):
        return "meow"
