"""
Sets in Python

Set is a collection of non repetitive elements

"""

a = {1, 2, 3, 4, 5, 1}

print(type(a))

print(a)

"""
Important: This syntax will create an empty dictionary and not an empty set

Properties of Sets

Sets are unordered
Sets are unindexed
There is no way to change items in sets
Sets cannot contain duplicate value
"""
b = {}

print(type(b))
"""
This will create an empty set
"""
c = set()
print(type(c))

#adding values to an empty set
c.add(4)
c.add(9)

"""
Hashable is a feature in Python objects that tells if the object has a hash value or not. A object is hashable if it has
a value that does not change during its entire lifetime.

List and Dictionary are not a hashable so cann't add in set

but tuple is hashable and can be added in set

"""
c.add((4, 5, 6))



print(c)

s = {10, 20, 40, 50}

print(len(s)) # print the length of this set

#remove method in Set
s.remove(20)
print(s)
#s.remove(9)

print(s.pop())


