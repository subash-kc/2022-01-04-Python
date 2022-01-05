# while <expression>:

# do work

import time

count = 0;


while True:
    if count == 5:
        break
    print(count)
    count = count + 1

    # count +=1
    time.sleep(1)
