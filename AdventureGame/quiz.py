'''
Dictionaries has key value pair, each key is a question and question has associated value and question has A, B , C, D
value
'''

quiz = {
    "Weapons Room":  ["What is the fastest animal in the world?: "                       , "B"],
    "Bedroom":       ["Who is known as the father of Computer?: "                        , "A"],
    "Kid's Bedroom": ["What is the tallest mountain in the world?: "                     , "D"],
    "Kitchen":       ["How many years did Franklin D. Roosevelt serve as a president?: " , "C"],
    "Garage":        ["Who was the first president to stay at the White House?: "        , "B"],
}

"""
2-D List to hold all the possible answers to each of these questions. List of list. Each list corresponds to the dictonary
of the questions
"""
question_answers = {
    "Weapons Room":  ["A. Leopard", "B. Cheetah", "C. Tiger", "D. Kangaroo"],  # all the options for 1st question
    "Bedroom":       ["A. Charles Babbage", "B. Bob Kahn", "C. Alan Turing", "D. Tim Cranner"], # all the options for 2nd question
    "Kid's Bedroom": ["A. Mount K2", "B. Mount Denali", "C. Mount Makalu", "D. Mount Everest"],  # all the options for 3rd
    "Kitchen":       ["A. 10", "B. 11", "C. 12", "D. 9"],  # all the options for 4th question
    "Garage":        ["A. George Washington", "B. John Adams", "C. Thomas Jefferson", "D. James Madison"] # all the options for 5th question
}