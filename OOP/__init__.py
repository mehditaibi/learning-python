# __init__ will automaticaly when we create a new instance of the class


class User:
    def __init__(self, first, last, age):
        self.name = first
        self.last = last
        self.age = age



user1 = User("John", "Smith", 68)
user2 = User("Joe", "Donald", 29)
user3 = User("Jordan", "Job", 32)
