# create the string hostname
hostname = "MTG"
# test logic with the `if` statement
# what to do if this statement is found to be true
if hostname == "MTG":
    print("The hostname was found to be MTG")


hostname1 = input("What value should we set for hostname1?")

if hostname1 == "MTG":
    print("The hostname was found to be MTG")


hostname2 = input("What value should we set for hostname2?")

if hostname2.lower()=="mtg":
    print("The hostname was found to be mtg")


## Collect input from user
hostname3 = input("What value should we set for hostname3?")

## use the lower method to test if input value matches expected value
if hostname3.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always print out to the user
print("Exiting the script")
