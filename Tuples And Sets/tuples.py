x = (1, 2, 3)
3 in x  # True
x[0] = 'Change me!'  # TypeError: 'tuple' object does not support item assignment
# It is immutable, faster than lists, can make code safer, communly used for unchanging data (e.g: months, seasons..)

alphabet = ('a', 'b', 'c', 'd')
type(alphabet)  # <class 'tuple'>
alphabet[0]  # 'a'

# LOOPING

names = ("John", "Matt", "Luc")

for name in names:
    print(name)

i = len(months) - 1

while i >= 0:
    print(months[i])
    i -= 1

# METHODS 

# count()
names.count("John") # 1

# index()
names.index("Matt") # 1 