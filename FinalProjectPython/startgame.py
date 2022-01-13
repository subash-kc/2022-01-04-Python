import time, os
from copy import deepcopy
from ColorIt import *
from quiz import quiz, question_answers

banner = open("banner.txt", "r").read()
print('')
print.green(banner)
print('')

gameinstructions_text = open("gameinstructions.txt", "r")
while(True):

    instruction_text = gameinstructions_text.read(1)
    if(instruction_text==""):
        break
    print(instruction_text, end="")
    time.sleep(0.005)
print("\n"*5)
# name = input("Please Enter your name: ")
name = 'Rob'

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


def clear():
    os.system('cls')


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

                clear()
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
                            print.blue('You win!')
                            return play_again()
                        else:
                            print.red('You lose! You didn\'t collect all the items.')
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