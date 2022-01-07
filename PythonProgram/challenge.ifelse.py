"""
If/Else challenge exercise
School Person Grade
"""
score = float(input("Enter the Score: \n"))


if score>=90 and score<=100:
    print("Your final grade is A")

elif score>=80 and score<90:
    print("Your final Grade is B")

elif score>=70 and score<80:
    print("Your final Grade is C")

elif score>=60 and score<70:
    print("Your final Grade is D")

elif score<60 and score>=0:
    print("Your final Grade is F")

else:
    print("Not a valid input")


## Slaffir-Simpson WindSpeed

"""
WindSpeed Challenge Exercise

"""
windspeed = int(input("Enter the Windspeeds in Km/hr: \n"))



def speed(windspeed):
    if 119>=windspeed:
        print("Invalid input")
    else:
        if windspeed>= 252:
            return "Five"
        elif windspeed>=209 and windspeed < 252:
            return "Four"
        elif windspeed>=178 and windspeed < 208:
            return "Three"
        elif windspeed>=154 and windspeed < 177:
            return "Two"
        elif windspeed>=119 and windspeed< 154:
            return "One"

print("WindSpeed Category is: ", speed(windspeed))

