# { __ : __ for __ in __ }

numbers = dict(first=1, second=2, third=3)
squard_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squard_numbers)  # {"first": 1, "second": 4, 'third': 9}


# CONDITIONAL LOGIC

num_list = [1, 2, 3, 4]
{num: ("even" if num % 2 == 0 else "odd") for num in num_list}
# {1: 'odd , 2: 'even', 3: 'odd', 4: 'even}
