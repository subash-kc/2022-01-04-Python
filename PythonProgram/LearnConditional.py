"""
if - We only want to do the code within the if block, if the conditional passed to the if statement remains True.
elif - Used along with the if statement. Short for, "else if". Within an if-elif-else block, only a single condition may ever be true.
else - Used in conjunction with if or if-elif. Works as a default 'catch all'.
while - Creates a loop, provided the conditional passed to while remains True.
assert - A statement that may be interpreted as, this conditional I am describing IS True. The assert statement is popular within testing frameworks.

"""

print("How many years have you been an employee: ")

emyears = int(input())

if emyears >= 30:
    vacadays = emyears *3
elif emyears>=20:
    vacadays = emyears *3
elif emyears>=10:
    vacadays = emyears * 1.5

else:
    vacadays = emyears *1

print('You have ', vacadays, ' vacation days')
