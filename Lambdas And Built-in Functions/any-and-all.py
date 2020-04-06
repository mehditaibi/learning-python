
# all,  returns True if all elements of the iterable are truthy ( or if the iterable is empty)

all([0, 1, 2, 3])  # False as 0 is falsy

all([char for char in 'eio' if char in 'aeiou'])

all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])

# any, returns True if any element of the iterable is truthy  ( if the iterable is empty returns False)

any([0, 1, 2, 3])  # True
