nums = [1, 2, 3]

# [__ for __ in __]

[x*10 for x in nums]  # [10, 20, 30]

name = 'john'

[char.upper() for char in name]  # ["J", 'O', 'H', 'N']

friends = ["ashley", 'matt', "michael"]

[friend[0].upper() for friend in friends]  # [ 'Ashley', 'Matt', 'Michael']

[num*10 for num in range(1, 6)]  # [ 10, 20, 30, 40, 50 ]

[bool(val) for val in [0, [], '']]  # [ False, False, False]


# LC WITH LOGIC

numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]

odds = [num for num in numbers if num % 2 != 0]

[num*2 if num % 2 == = 0 else num / 2 for num in numbers]
