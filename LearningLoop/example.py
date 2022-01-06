pets = ["Fluffy the cat", "spot the dog", "leonard the llame"]

foo = open("mypets.txt", "w")

with open("mypets.txt", "w") as petfile:
    print("My cute pets!", file=petfile)
    intro = "Here is a list of my pets"
    petfile.write(intro)
    print()
    petfile.writelines(pets)

    for pet in pets:
        petfile.write(f"\n{pet}")