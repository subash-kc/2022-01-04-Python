## make it easy to write user-friendly commoand-lin interfaces. the program defines what arguments is required

import argparse

def parze():
    parser = argparse.ArgumentParser(description="Choose your Reading")
    parser.add_argument("greeting", default="1", help="Pick 1 for 'Hi', 2 for 'Pirately Hello' ")
    parser.add_argument("----Bye----", default=False, help="Say Bye?")
    return parser.parse_args()

def say_hi():
    return "Hello There!"

def say_argh():
    return "Aargh! Ahoy ye mateys"

if __name__ == '__main__':
    args = parze()
    print(args)
    print(args.greeting)
    #greeting = input("What greeting should we use?\n1: 'Hi'\n2: ' Pirately hello'")

    #if greeting == "1":
       # print(say_hi())
    #elif greeting =="2":
        #print(say_argh())