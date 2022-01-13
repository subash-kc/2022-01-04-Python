import time, os
from copy import deepcopy
from ColorIt import *
from quiz import quiz, question_answers

banner = open("banner.txt", "r").read()
print('')
print.green(banner)
time.sleep(5)
print('')

gameinstructions_text = open("gameinstructions.txt", "r")
while(True):

    instruction_text = gameinstructions_text.read(1)
    if(instruction_text==""):
        break
    print(instruction_text, end="")
    time.sleep(0.005)
print("\n"*3)
name = input("Please Enter your name: ")

print("Welcome to Mission Escape", name, "Good Luck!!!!")

time.sleep(3)

# def clear_screen(lines):
#     for l in range (lines):
#         print(l)

def showInstructions():
    """Show Instructions when called"""
    print(f'''
    Welcome again {name} House Escape Game
    Please read these instructions in order to successfully escape for the house.
    =============================================================================
    Commands:
    go [direction]
    get [item]
    No need to add go if there is a set of directions. Example [kid's bedroom, stairs], enter only stairs or Kid's Bedroom.
    You will have 2 opportunity unlock the door if failed you lose.
          
       ''')
    time.sleep(3)
    print("Games Rules")
    print.red("To win the game you must need to escape from the house.")
    print.red("You also must need to collect all the items before escaping from the house.")
    print.red("You will not able to go back to rooms once you are in kitchen room.")

    time.sleep(10)

    print("\n" * 1)
    get_answer = input("Do you wish to continue(Yes/No): ")

    if get_answer == "Yes".lower():
        showStatus()
    else:
        print('')
        print("Thank you for choosing Home Escape Game Mission!!!!!")
        exit()

# def clear():
#     os.system('cls')


def showStatus():
    """Determine the current status of the player"""
    print("--------------------------------------------------------------------------------------")
    print.yellow(f'You are in the {currentRoom}.')
    print(f"Inventory: {list(inventory)}")

    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    print("--------------------------------------------------------------------------------------")

#Inventory is initially Empty
inventory = set()

#a dictionary that is linking a room to othe rooms
rooms = {
    "Office Room" : {
        "left"     : "Weapons Room",
        "right"    : {"Kid's Bedroom", "Stairs"},
        "straight" : "Bedroom",
        "items"    : ["Wallet"]
    },
    "Weapons Room" : {
        "right"    : {"Office Room", "Stairs"},
        "left"     : "Bedroom",
        "items"    : ["Weapon"]
    },

    "Bedroom" : {
        "straight" : {"Office Room", "Kid's Bedroom"},
        "left"     : "Stairs",
        "right"    : "Weapons Room",
        "items"    : ["Spouse"]
    },

    "Kid's Bedroom" : {
        "left"     : {"Office Room", "Weapons Room"},
        "right"    : "Stairs",
        "straight" : "Bedroom",
        "items"    : ["Kids"]
    },

    "Stairs" : {
        "down"     : "Kitchen",
    },

    "Kitchen" : {
        "down"     : "Garage",
        "up"       : "All Rooms",
        "items"    : ["Foods"]
    },

    "Garage" : {
        "up"       : "Kitchen",
        "straight" : "Outside",
        "items"    : ["Key", "Car"]
    },

    "Outside" : {}

}

currentRoom = ''

def play():
    global currentRoom
    currentRoom = "Office Room"
    questions = deepcopy(quiz)
    showInstructions()

    while True:
        showStatus()

        # answer = input("You are in the Office Room, the game is on. You seee bunch of bad Zombies coming to your way. What way would you like to go? ").lower()

        directions = rooms[currentRoom]
        for d, options in directions.items():
            if type(options) == str:
                options = [options]
            present = ' and '.join(options)
            if present:
                print.green(f"{d.capitalize()} is {present}.")

        while True:
            answer = input('What would you like to do? ').lower()
            if answer:
                command_target = answer.split(' ')
                if len(command_target) == 2:
                    command, target = command_target
                    if command in ['go', 'get']:
                        break
                    else:
                        print.red("Invalid command.")
                else:
                    print.red("Invalid command.")


        if command == "go":
            if target in directions:

                destination = directions[target]

                if type(destination) == set:

                    for r in destination:
                        print.green(r)

                    while True:

                        room = input('Which room would do you go to? ')

                        found = False
                        broken = False
                        for r in destination:
                            if room.lower() == r.lower():
                                destination = r
                                found = True
                                broken = True
                                break

                        if broken:
                            break

                # clear_screen()
                question_answer = questions.get(destination)

                if question_answer:

                    print('')
                    print.red('Oh snap the door is locked! You must answer correctly to unlock the door.')
                    print.red('You have 2 lives left.')

                    question, answer = question_answer

                    choices = question_answers[destination]
                    print.yellow(question)

                    for choice in choices:
                        print.green(choice)

                    lives = 2
                    while True:
                        if lives > 0:

                            while True:
                                attempt = input('')
                                if attempt.upper() in ['A', 'B', 'C', 'D']:
                                    break
                                else:
                                    print.red('Invalid choice. Type A, B, C or D.')

                            if attempt.upper() == answer:
                                questions.pop(destination)
                                print.blue('Correct!')
                                break
                            else:
                                print.red('Incorrect!')
                                lives -= 1
                                print.red(f'You have {lives} lives left.')
                        else:
                            print.red('The zombies got you and your family!')
                            print.red('GAME OVER')
                            return play_again()

                else:
                    if destination == 'Outside':
                        if inventory == {"Wallet", "Weapon", "Spouse", "Kids", "Foods", "Key", "Car"}:
                            print.blue('You win!', "You along with your family successfully escaped from the town. "
                                                   "Congratulations")
                            return play_again()
                        else:
                            print.red('You lose! You didn\'t collect all the required items to escape.', "You and your family didn't survive")
                            return play_again()

                currentRoom = destination

            else:
                print.red("You can't go that way!!!")

        elif command == "get":
            items = rooms[currentRoom]['items']

            found = False
            for item in items:
                if target.lower() == item.lower():
                    target = item
                    found = True
                    break

            if found:
                if target in inventory:
                    print("You have already taken that item ")
                else:
                    inventory.add(target)

                    index = items.index(target)
                    items.pop(index)

                    print.blue(f"{target} received!!!!")
            else:
                print.red('That item is not here.')


def play_again():
    while True:
        option = input('Do you want to play again? [Y/N]: ').lower()
        if option in ['y', 'n']:
            if option == 'y':
                return play()
            else:
                return

play()