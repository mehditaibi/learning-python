dog = {
    "name": "Rex",
    "age": 2,
    "color": "Black"
}

# Clear => Clears all the keys and values

dog.clear()

# Copy => copy the dictionary

cat = dog.copy()
cat === dog # True 
cat is dog # False 

# fromkeys => Creates a dictionary from comma separeated values

{}.fromkeys(["a", "b"], 'unknown') #  { a: 'unknown', b: 'unknown'}

# get() => getter 

dog.get("name") # "Rex"
dog.get("email") # None

# pop() => Removes key value pair and returns the value

dog.pop("color") # "Black"


# popItem() => removes a random key value pair

dog.popitem()

# update() => Takes all key value pair and copies it 

cat.update(dog) # cat = {"name": "Rex","age": 2,"color": "Black"} // doesn't remove but overides all existing key value pair


