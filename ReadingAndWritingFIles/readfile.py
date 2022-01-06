myfile = open('text.txt', 'r')

readlist = myfile.readlines()

for read in readlist:
    print(read)
