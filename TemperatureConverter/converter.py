"""
This program converts temperature from Celcius to Farenheit and Vice-Versa
"""

def fehrenheit(c):
    return (c*9/5)+32

def celcius(f):
    return (f-32)*5/9

i = 0
while i==0:
    print("1. For convert celsius to faherenheit: ")
    print("2. For convert faherenheit to celsius: ")
    while True:
        choice= int(input("Enter your choice(1 or 2): \n"))

        if(choice==1):
            temp1=int(input("Enter Temperature in Celcius: \n"))
            print("The temperature in fahernheit =", fehrenheit(temp1), "F")

        if(choice==2):
            temp2 = int(input("Enter temp in Fahrenheit: \n"))
            print(f"The temperature in celsius is {celcius(temp2)}C")

        if(choice>2):
            i=1
            print("Enter a Valid Choice!!")
            continue
        convert_again = input("Do you want to convert another Temperature again? (yes/no): ").lower()

        if convert_again != "yes":
            break
        print()

    print("Thank you for using the app. Please rate our app and gives us a feedback. Thank you.")
    exit()




