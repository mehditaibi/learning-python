class Person:
    def __init__(self):
        self._secret = "hi!"  # appending _ means that this is a private attribute by convention
        self.name = "Tony"
        self.__msg = "I like turtles"  # 2 __ is for name mangling, only accesible by the class not accessible by the instances 


p = Person()

print(p.name)
print(p._secret)
