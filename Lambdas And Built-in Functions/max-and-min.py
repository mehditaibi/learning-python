# max, returns the largest item in an iterable or the largest of two or more arguments

nums = [40, 23, 23, 234]

max(nums)  # 234
min(nums)  # 23

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
min(len(name) for name in names)  # 3

# find the longest name itself
max(names, key=lambda n: len(n))  # Ollivander

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
# {"title": "happy birthday", "playcount": 1}
min(songs, key=lambda s: s['playcount'])

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title']  # YMCA
