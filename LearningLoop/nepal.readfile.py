readfile = open("nepal.txt", "r")

readlist = readfile.readlines()

for read in readlist:
    print(read, end="")