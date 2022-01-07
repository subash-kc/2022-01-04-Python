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
print("Names: ", munsters["names"])

print("EndDate: ", munsters["endDate"])

print("StartDate: ", munsters["startDate"])

munsters["episodes"] = 70

print("All Keys and Values in Musters", munsters)

def main():
        #Display the names
        print(munsters.get("names"))

        #Display the startdate
        print(munsters.get("endDate"))

        #Display the endDate
        print(munsters.get("startDate"))

        #Add key
        munsters["episodes"] = 70

        print(munsters.get("episodes"))

main()