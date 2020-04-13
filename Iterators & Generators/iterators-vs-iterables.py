# Iterator 
# an object that can be iterated upon. An object
# which returns data, one element at a time when
# next() is called in it

# Iterable 
# An object which will retun an iterator when 
# iter() is called on it 

# "HELLO" is an iterable, but it is not an iterator
# iter("Hello") returns an iterator

name = "Oprah"

next(name) # throws an error
it = iter(name) # returns an iterator

# NEXT 
# When next() is called on an iterator, the 
# iterator returns the next item. It keeps 
# doing so until it raises a StopIteration error.

next(it) # O
next(it) # p
next(it) # r
next(it) # a
next(it) # h

