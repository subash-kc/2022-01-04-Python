#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------

"""
Display the value mapped to names
Display the value mapped to endDate
Display the value mapped to startDate
Add a new key, episodes mapped to the value of 70

"""
print(munsters["names"])

print(munsters["endDate"])

print(munsters["startDate"])

munsters["episodes"] = 70;

print(munsters)