class Truck: #when defining object starting with capital

    #key about method in class always starts with self and enclose within a class
    def __init__(self, name, style, wheels: int = 4): #certain ability and characteristics
        self.name = name
        #print("You just built a truck!!!")
        self.style = style
        self.wheels = wheels
        self.pos = 0

    def __repr__(self):
        return f"{self.name}: {self.pos}"

    def go_forward(self, count):
        self.pos += count

print("\nMaking Mater")
mater = Truck("Tow Mater", "tow truck")
print(mater)
print(mater.name)
print(mater.style)

print("\nMaking Mack")
mack = Truck("Mack", "Transport Semi")
print(mack)
print(mack.name)
print(mack.style)
mack.go_forward(3)
print(mack)
