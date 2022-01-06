## create file object in "r"ead mode

#!/usr/bin/env python3
## create file object in "r"ead mode

cfg_file = input("what file do you want to read?:\n")

#with open(input("what file do you want to read?\n"), "r") another way to do it 0 additional lines

with open(cfg_file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

count = 0
for item in configlist:
    count +=1

print(f"There are {count} lines in this file")

num_lines = len(configlist)
print(f"Using the len() function, we see ther are: {num_lines} lines")

# ooption 3 - 1line

print(f"On a single line, using len() function, we find there are {len(configlist)}")

