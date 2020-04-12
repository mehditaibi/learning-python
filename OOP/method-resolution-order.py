# METHOD RESOLUTION ORDER (MRO)
# Whenever you create a class, Python sets a Mehtod Resolution Order, or MRO for that class,
# Which is the order in which Python will look for mehtods on instances of that class.

# You can programmatically reference the MRO in three ways:

# - __mro__ attrivute on the class
# - use the mro() method on the class
# - use the builtin help(cls) method


class A:
    def do_something(self):
        print("Method Defined In: A")


class B(A):
    def do_something(self):
        print("Method Defined In: B")


class C(A):
    def do_something(self):
        print("Method Defined In: C")


class D(B, C):
    def do_something(self):
        print("Method Defined In: D")


thing = D()
thing.do_something()
