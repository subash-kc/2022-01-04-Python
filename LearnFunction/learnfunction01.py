"""
Function are subprograms which are used to compute a value or perform a task.

Type of Functions:-

Built in Functions:
       print(), upper()

User define functions

Advantage of Functions

1. Write once and use it as many time as you need. This provides code reusability
2. Function facilitates ease of code maintenance
3. Divide Large task into many small task so it will help you to debug code
4. You can remove or add new feature to a function anytime.

"""

"""
We can define a function using def keyword followed by function name with parentheses. This is also called
as Creating a function, Writing a Function, Defining a FUnction.

Syntax:-
def function_name():
    Local Variable
    block of statement
    return(variable or expression)

def function_name(param1, param2, param3, .....)
    Local Variable
    Block of statement
    return (variable or expression)

Note - Nooed to mainitain a proper indentation   
"""


# creating a list

def add():
    list = [8, 2, 3, 0, 7]

    total = 0;

    for i in range(0, len(list)):
        total = total + list[i]
    print('Sum of all elements in given list: ', total)


if __name__ == '__main__':
    add()
print()


# another method

def sum_list():
    mylist = [8, 2, 3, 0, 7]

    # Using inbuilt sum method
    total = sum(mylist)

    print("Sum of all elements in given list1: ", total)


if __name__ == '__main__':
    sum_list()
print()


def multiplylist():
    list_multiply = [8, 2, 3, -1, 7]
    total = 1;

    for x in list_multiply:
        total = total * x

    print(total)


if __name__ == '__main__':
    multiplylist()

# Method 2: Unsing numpy.prid() ^ Install numpy package

import numpy


def product_total():
    list_product = [8, 2, 3, -1, 7]

    total = numpy.prod(list_product)

    print("Another method using numpy method to find product in list: ", total)


product_total()

print()


def findingminmax(num1: int, num2: int, num3: int) -> int:
    max = 0;

    if (num1 > num2 and num1 > num2):
        max = num1
    elif (num2 > num1 and num2 > num3):
        max = num2
    else:
        max = num3

    print("The maximum number in given list is: ", max)


findingminmax(22, 26, 30)

print()
print("Another Method to find maximum")


def findingmaximum(num1: int, num2: int, num3: int) -> int:
    find_max_list = (num1, num2, num3)

    return max(find_max_list)


x = int(input("Enter your first Number: "))

y = int(input("Enter your second Number: "))

z = int(input("Enter your third Number: "))

print("Maximum number is ::>", findingmaximum(x, y, z))


"""Python program to print the even numbers from a given list"""

def find_even():
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for num in sample_list:

        if num % 2 == 0:
            print(num, end=" ")

find_even()

print()
"""
Pythhon program to find prime numbers in given list
Function should return true if the number is prime; else false
"""

def isPrime(num):

    if (num < 2):
        return True

    for i in range (2, num//2+1):
        if(num%i==0):
            return False
    return True

number =int(input("Enter the number you will like to check whether the number is prime or not: \n"))

if isPrime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime number")


"""
Another Method to find prime number
"""

