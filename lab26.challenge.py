"""
Challenge Part
"""

round2 = 0
answer2 = " "

# augment our while condition to test if "brian" or "shrubbery" was the input
# you could reduce the complexity of this conditional with some "break" statements
while round2 < 3 and (answer2 != "Brian" and answer2 != "Shrubbery"):
    round2 += 1     # increase the round counter by 1
    answer2 = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer2 = answer2.capitalize() # this line inserted to line 8 will make all
                                 # user input starts with an uppercase
    if answer2 == "Brian": # logic to check if user gave correct answer
        print("Correct!")
    elif answer2 == "Shrubbery":
        print("You gave the super secret answer!")
    elif round2 == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")