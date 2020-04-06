# sorted (works on anything that is iterable)

more_numbers = [6, 1, 8, 2]
sorted(more_numbers)  # [1,2,6,8]
print(more_numbers)  # [6, 1, 8, 2]

users = [
    {"username": "samuel", "tweets": [
        "I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# To sort users by their username
sorted(users, key=lambda user: user['username'])

# Finding our most active users...
# Sort users by number of tweets, descending
sorted(users, key=lambda user: len(user["tweets"]), reverse=True)

