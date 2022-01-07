#userInput in Python

name = input("What is your name?: ")

age = int(input("How old are you?: "))

height = float(input("How tall you are?: "))

#after casting to integer then we can perform mathematical operation
age = age + 1;

print("Hello " + name, age)

print("You are " + str(age) + " years old " + "and " + str(height) + " foot tall.")