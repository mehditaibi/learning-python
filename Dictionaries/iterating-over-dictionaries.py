dog = {
    "name": "Rex",
    "age": 2,
    "color": "Black"
}

for value in dog.values():
    print(value)


for key in dog.keys():
    print(key)

for key, value in dog.items():
    print(f"Key: {key}, Value: {value}")
