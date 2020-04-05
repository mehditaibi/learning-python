# No order, no duplicate values, no index

numbers = set({1, 2, 3, 4, 4, 4})  # {1,2,3,4}
1 in numbers  # True

# LOOPING

for number in numbers:
    print(number)

# METHODS

# add()
numbers.add(5)

# remove()
numbers.remove(5)  # throws an error if item is not present

# copy()
numbers_v2 = numbers.copy()

# clear()
numbers_v2.clear()

# Set Math
|  # union, it will iterate over two sets and return a new set removing all duplicates
&  # and, it will iterate over two sets and return a new set with all the duplicates


# Set Comprehension

{x**2 for in range(10)}
