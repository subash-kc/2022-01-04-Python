import os

path = "C:\\Users\\mksubash\\Desktop\\folder"

if os.path.exists(path):
    print("That location exists!!!")

    if os.path.isfile(path):
        print('That is a file')
    elif os.path.isdir(path):
        print("that is a folder directory!!!")

else:
    print("That location doesnt' exists!!!")
