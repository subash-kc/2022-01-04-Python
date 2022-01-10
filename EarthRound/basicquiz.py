print("-----------------------------------------------------------")

"""
Defining all the necessary to function
new game function to start the game
"""


def clear_screen(lines):
    for l in range(lines):
        print()

def new_game():
    # guesses is empty list in the beginning
    guesses = []
    # correct guesses set to 0 . we haven't guesssed anything
    correct_guesses = 0
    question_number = 1  # represent the first question

    # We need to display all the questions in our dictionary of questions
    clear_screen(20)
    for key in questions:
        clear_screen(35)
        print()
        print(key)

        # nested for loop to display all the options. Indexing starts from 0. Use some sorts of counter
        for i in options[question_number - 1]:
            print(i)

        # User input to prompt the choices
        guess = input("Enter (A, B, C, or D): ").upper()  # String case sensitive and give them a point
        guesses.append(guess)  # emplty list og guesses and apend our guess

        # calling check answer function to check answer by passing few answers argument.
        # incrementing correct guesses by one
        correct_guesses += check_answer(questions.get(key), guess)
        # incrementing by 1
        question_number += 1

    display_score(correct_guesses, guesses)


# --------------------------------------------------------------
"""
Function to check the answer

"""


# parameter of answer and guess
def check_answer(answer, guess):
    # checking our answer to the correct answer
    if answer == guess:
        print("Your answer is CORRECT!!!!")
        # return 1 point if we scored a point
        return 1
    else:
        print("You gave a WRONG answer!!!")
        # donot get a point if we donot score a point
        return 0


# --------------------------------------------------

"""
Function to Display Score
"""


def display_score(correct_guesses, guesses):
    print("-------------------------------")
    # print("RESULTS")
    print("------------------------------------------------")

    # print("Answers: ", end=" ")

    # for i in questions:
    # print(questions.get(i), end=" ")
    # print()

    print("Your Answer: ", end="")

    for i in guesses:
        print(i, end=" ")
    print()
    score = (correct_guesses) * 100

    print("Your score is: " + str(score))


# ------------------------------------------------------------

"""
Function to ask user to play again
"""


def play_again():
    response = input("Do you want to play again? (yes or no): ").upper()

    if response == "YES":
        return True
    else:
        return False


# -----------------------------------------------------------

'''
Dictionaries has key value pair, each key is a question and question has associated value and question has A, B , C, D
value
'''
questions = {
    "What is the fastest animal in the world?: ": "B",
    "Who is known as the father of Computer?: ": "A",
    "What is the tallest mountain in the world?: ": "D",
    "How many years Franklin D. Roosevelt serve as a president?: ": "C",
    "Who was the first president to stay at the White House?: ": "B"
}

"""
2-D List to hold all the possible answers to each of these questions. List of list. Each list corresponds to the dictonary
of the questions
"""
options = [["A. Leopard", "B. Cheetah", "C. Tiger", "D. Kangaroo"],  # all the options for 1st question
           ["A. Charles Babbage", "B. Bob Kahn", "C. Alan Turing", "D. Tim Cranner"],
           # all the options for 2nd question
           ["A. Mount K2", "B. Mount Denali", "C. C. Mount Makalu", "D. Mount Everest"],  # all the options for 3rd
           ["A. 10", "B. 11", "C. 12", "D. 9"],  # all the options for 4th question
           ["A. George Washington", "B. John Adams", "C. Thomas Jefferson",
            "D. James Madison"]]  # all the options for 5th question

new_game()

while play_again():
    new_game()

print("GAME OVER. BYEEEEE")
