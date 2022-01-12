import time

gameinstructions_text = open("gameinstructions.txt", "r")

while(True):
    instruction_text = gameinstructions_text.read(1)
    if(instruction_text==""):
        break
    print(instruction_text, end="")
    time.sleep(0.005)
print("\n"*5)
name = input("Please Enter your name: ")

print("Welcome to Mission Escape", name, "Good Luck!!!!")

def showInstructions():
    """Show Instructions when called"""
    print('''
       House Escape Game
       ========
       Commands:
         go [direction]
         get [item]
       ''')
    print("To win the game you must need to escape from the house.")
    print("You also must need to get key, wallet, get family and weapon to escape from the house.")

def showStatus():
    """Determine the current status of the player"""
    print("--------------------------------------------------------------------------------------")
    print('You are in the ' + currentRoom)
    print("Inventory: " + str(inventory))

    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    print("-------------------------------------------------------------------------")

#Inventory is initially Empty
inventory = []

#a dictionary that is linking a room to othe rooms
rooms = {
    "Office Room" : {
        "left" : "Weapon Room",
        "right" : {"Kid's Bedroom", "Stairs"},
        "straight" : "Bedroom",
        "item" : "Wallet"
    },
    "Weapon Room" : {
        "right" : {"Office Room", "Stairs"},
        "left" : "Bedroom",
        "item" : "Weapon"
    },

    "Bedroom" : {
        "straight" : {"Office Room", "Kid's Room"},
        "left" : "Stairs",
        "right" : "Weapon Room",
        "item" : "Spouse"
    },

    "Kid's Room" : {
        "left" : {"Office Room", "Weapon's Room"},
        "right" : "Stairs",
        "straight" : "Bedroom",
        "item" : "Kids"
    },

    "Stairs" : {
        "down" : "Kitchen",
    },

    "Kitchen" : {
        "down" : "Garage",
        "up" : "Rooms",
        "item" : "Foods"
    },

    "Garage" : {
        "up" : "Kitchen",
        "item" : {"Key", "Car"}
    }

}

currentRoom = "Office Room"

showInstructions()

while True:
    showStatus()

    answer = input("You are in the Office Room, the game is on. You seee bunch of bad Zombies coming to your way. What way would you like to go? ").lower()

    if answer[0] == "go":
        if answer[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][answer[1]]
        else:
            print("You can't go that way!!!")

    if answer[0] == "get":
        if "item" in rooms[currentRoom] and answer[1] in rooms[currentRoom]["item"]:
            inventory += [answer[1]]
        # there is no door link to the direction you input
            print(answer[1] + "Received!")

        else:
            print("You can't go that way!!!!")
