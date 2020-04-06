l = [1, 2, 3, 4]

evens = list(filter(lambda x: x % 2 == 0, l))

evens  # [2,4]


names = ["Lassie", "Colt", "Rusty"]

list(map(lambda name: f"Your instructor is {name}", filter(
    lambda value: len(value) < 5, names)))
