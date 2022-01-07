
#Using with open the file closes automatically but won't handle any exception or error

try:
    with open("test.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")
