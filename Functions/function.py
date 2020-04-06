from random import random


def flip_coin():
    if random() > .5:
        return "Heads"
    else:
        return "Tails"


print(flip_coin())


def square(num):
    return num * num


print(square(4))


def exponent(num, power=2):
    return num ** power


def full_name(first, last):
    """"returns the first and last name given"""
    return f"Hello {first} {last}"


full_name(last="Doe", first="John")
full_name.__doc__  # returns the first and last name given


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner()


# *
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total
# returns all the arguments as a list

# **kwargs
def fav_colors(**kwargs):
    print(kwargs)
# returns all the arguments as a dictionnary


# Unpacking a tuple 
nums = (1,2,3,4,5,6)
sum_all_nums(*nums) # the * operator unpack the tuple similar to the spread operator in JS 

# ** to unpack dictionaries 
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "John", "second": "Sara"}

display_names(names) # Throw an error 
display_names(**names) # It works!  
