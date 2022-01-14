import time
from copy import deepcopy  # creating a copy so one can change one copy without changing the other
from ColorIt import *
from quiz import quiz, question_answers
from rooms import rooms

banner = open("banner.txt", "r").read()
print('')
print.green(banner)
time.sleep(2)
print('')

gameinstructions_text = open("gameinstructions.txt", "r")
while (True):

    instruction_text = gameinstructions_text.read(1)
    if (instruction_text == ""):
        break
    print(instruction_text, end="")
    time.sleep(0.0005)
print("\n" * 3)
name = input("Please Enter your name: ")

print("Welcome to Mission Escape", name, "Good Luck!!!!")

time.sleep(5)


def showInstructions():
    """Show Instructions when called"""
    print(f'''
    Welcome again {name}, House Escape Game
    Please read these instructions in order to successfully escape for the house.
    =============================================================================
    Commands:
    go [direction]
    get [item]
    No need to add go if there is a set of directions. Example [kid's bedroom, stairs], enter only stairs or Kid's Bedroom.
    You will have 2 opportunity unlock the door if failed you lose.

       ''')
    # time.sleep(3)
    print("Games Rules")
    print.red("To win the game you must need to escape from the house.")
    print.red("You also must need to collect all the items before escaping from the house.")
    print.red("You will not able to go back to rooms once you are in kitchen room.")

    # time.sleep(10)

    print("\n" * 1)

    while True:

        get_answer = input("Do you wish to continue(Yes/No): ").lower()
        if get_answer == "yes":
            break
        elif get_answer == "no":
            print('')
            print("Thank you for choosing Home Escape Game Mission!!!!!")
            exit()
        else:
            print("Invalid Command!!!!")
            print("Enter (yes/no) to continue: ")

    time.sleep(5)

    cls()


def showStatus():
    """Determine the current status of the player"""
    print("--------------------------------------------------------------------------------------")
    print.yellow(f'You are in the {currentRoom}.')
    print(f"Inventory: {list(inventory)}")

    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    print("--------------------------------------------------------------------------------------")


# Inventory is initially Empty
inventory = set()  # empty set in the beginning and helps to any of the iterable to sequence of iterable elements with
                    # distinct element.
# inventory = {"Wallet", "Weapon", "Spouse", "Kids"}

currentRoom = ''


def cls():
    print("\n" * 100)


def play():
    global currentRoom
    currentRoom = "Office Room"
    questions = deepcopy(quiz)
    showInstructions()

    while True:
        showStatus()

        # Add items to the list and make it as a preset inventory
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
                # split an inputted string
                command_target = answer.split(' ')
                if len(command_target) == 2:
                    command, target = command_target
                    if command in ['go', 'get']:
                        break
                    else:
                        print.red("Invalid command.")
                else:
                    print.red("Invalid command.")

        # when command is go, it gives a direction to move left or right
        if command == "go":

            # Destination set as the target
            destination = directions.get(target)

            # this is validation check once in kitchen and stays in kitchen, once in kitchen Player can't go up.
            if destination == 'All Rooms' and target == 'up':
                print.red('You cannot go that way. You have collected all the items.')
                destination = 'Kitchen'

            if destination:

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

                question_answer = questions.get(destination)

                # Quiz fromm quiz.py
                if question_answer:
                    time.sleep(2)
                    print('')
                    cls()
                    print.red('Oh snap the door is locked! You must answer correctly to unlock the door.')
                    print.red('You have 2 lives left.')

                    question, answer = question_answer

                    choices = question_answers[destination]
                    print.yellow(question)

                    for choice in choices:
                        print.green(choice)

                    # Initial lives is 2 and decrements on wrong answer
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
                                print.green("You unlocked the door.")
                                time.sleep(3)
                                cls()
                                break
                            else:
                                print.red('Incorrect!')
                                lives -= 1
                                print.red(f'You have {lives} lives left.')
                        else:
                            print.red('The zombies got you, and your family!')
                            print.red('GAME OVER')
                            return play_again()

                # validation check in Stairs if Player has Received all the Items or not before proceeding forward.
                elif destination == "Stairs":
                    if inventory == {"Wallet", "Weapon", "Kids", "Spouse"}:
                        print("You have collected all the items from 3rd Floor.")
                    else:
                        print.red(
                            "You haven't collected all the items. Go back and Collect all the items. Otherwise, you"
                            "will be not able to escape from the town.")
                        # print.red("Game Over")
                        # return play_again()

                # Validation check when destination is outside and Player has received all the items or not.
                else:
                    if destination == 'Outside':
                        if inventory == {"Wallet", "Weapon", "Spouse", "Kids", "Foods", "Key", "Car"}:
                            print.blue('You win!', "You along with your family successfully escaped from the town. "
                                                   "Congratulations")
                            return play_again()
                        else:
                            print.red('You lose! You didn\'t collect all the required items to escape.',
                                      "You and your family didn't survive")
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

            # Check if the Player already has Received the items in the rooms.
            if found:
                if target in inventory:
                    print("You have already taken that item ")
                else:
                    inventory.add(target)

                    index = items.index(target)
                    items.pop(index)

                    print.blue(f"{target} received!!!!")
                    time.sleep(3)
                    cls()
            else:
                print.red('That item is not here.')


# Play again function to ask user to play the game again
def play_again():
    while True:
        option = input('Do you want to play again? [Y/N]: ').lower()
        if option in ['y', 'n']:
            if option == 'y':
                return play()
            else:
                return

if __name__ == '__main__':
    play()
