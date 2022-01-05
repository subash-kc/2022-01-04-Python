#!/usr/bin/env python3

a = "the prime directive"

a = a.split(" ") # a is converted to a list of strings

print(a)

a = "-".join(a) # is the result of using "-" to glue together a list of string

print(a)


# create a small string
name = "Alta3 Research offers classes on Python coding"
newlist = name.split(" ") # this returns a list
print(newlist)

# create a list of strings
myiplist = ["192", "168", "0", "12"]

# set singleip as the result of joining the list myiplist around the "."
singleip = ".".join(myiplist)

# display singleip
print(singleip)

"""
Above Example with Best Practices
"""

def main():
   """ Run-time code"""
   # create a small string
   str1 = "Alta3 Research offers classes on Python coding"
   newlist = str1.split(" ") # this returns a list
   print(newlist)

   # create a list of strings
   list1 = ["192", "168", "0", "12"]
   # set singleip as the result of joining the list myiplist around the "."
   singleIp = ".".join(list1)
   # display singleip
   print(singleIp)

# call our main function
main()