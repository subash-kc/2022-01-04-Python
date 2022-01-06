# dictionary = A changeable, unordered collection of unique key: value paris fast because they are hasing, allow us to
# to access a value quickly

capitals = {"USA": "Washington DC",
            "Nepal": "Kathmandu",
            "India": "New Delhi",
            "Russia": "Moscow",
            "Japan": "Tokyo"}

print(capitals["Russia"])

#get method is the safest way to access values in Dictionaries
print(capitals.get("Germany"))

#to print all the keys in dictionaries
print(capitals.keys())

#to print all the values in dictionaries
print(capitals.values())

#to print all keys and values pairs in dictionaries
print(capitals.items())

# another way to access key value pairs is for loop
for key,value in capitals.items():
    print(key, value)

print()

capitals.update({"Germany": "Berlin"})

print(capitals.items())

print()

# To print just keys in dictionaries
for key in capitals.keys():
    print(key)

print() # this empty print method prints empty blank line and make it clean

#to print just values in dictionaries
for value in capitals.values():
    print(value)

print()

capitals.update({"Nepal": "Chitwan"})

for key,value in capitals.items():
    print(key, value)

print()
#to remove key, value from the dictionary
capitals.pop("India")

print(capitals)

print()

#to create a copy of hte same items.
new_capitals = capitals.copy()

print(new_capitals)

capitals_clear = capitals.clear()

print(capitals_clear)