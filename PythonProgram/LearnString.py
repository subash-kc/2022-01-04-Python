#Collection of Characters

example = 'Learning Python with Single Quotes'

example2 = "Learning Python wiht Double Quotes"

#delimiters hte quotes in outside

example3 = 'Learning "Python" with single Quotes'

example4 ="Learning \"Python\" with \n"

better = " This one has a \"double quote\" in it"

best = 'This is the best way to "double quote" something different'



print(best)

best_upper = best.upper()

print(best_upper)

#print(best_upper)



paragraph = example + example2 + example3
print(paragraph)

pretty_para = example + ", " + example2 + ", " + example3
print(pretty_para)

name = "fluffy"
age = 7;
color = "white"

myCat = "My cat is named" + name + " and is the color " + color + " and is " + str(age) + " years old."
print(myCat)

#f string doesnt have to force to concate to String. Best way
yourcat = f"Your cat is named {name} and is the color {color} and is {age} years old."
print(yourcat)

bdayat = f"Your cat is named {name} and is the color {color} and just turned {age + 1} years old."
print(bdayat)

#format method
hiscat = "His cat is named {} and is the color {} and is {} years old.".format(name, color, age)
print(hiscat)

cats = ["fluffy", "snowball", "garfield"]
kitty = "My cats are : {}, {}, and {}".format(*cats)
print(kitty)

#* unpacked the argument of the list(this)
diff_order = "My cats are : {1}, {2}, and {0}".format(*cats)
print(diff_order)

movie = "Usual Suspects    "
print(movie)

print(movie[4:12])

print(movie[::2])

print(movie[-1::-1])

#remove the whiteSpace
print(movie.strip(), end="***\n")

#splits int a list based on a str
print(movie.split('e'))

#remove whitespace and split into a list based on a str
split_movie = movie.strip().split('e')
print(split_movie)

print('***'.join(split_movie))

