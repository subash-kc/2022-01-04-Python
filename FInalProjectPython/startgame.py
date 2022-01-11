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
