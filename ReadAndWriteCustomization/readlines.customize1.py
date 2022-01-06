
######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()

#customizze 1

## Iterate through configlist
for x in configlist:
    print(x, end="")

#Customize 2

print()

print("-----------From here customize 2 starts---------------------------")

## Iterate through configlist
for x in configlist:
    print(x.strip())
