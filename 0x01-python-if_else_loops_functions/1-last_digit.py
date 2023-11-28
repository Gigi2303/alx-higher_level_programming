#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    rac = number % (-10)
else:
    rac = number % 10

if rac > 5:
    print(f"Last digit of {number} is {rac} and is greater than 5")

elif rac == 0:
    print(f"Last digit of {number} is {rac} and is 0")

else:
    print(f"Last digit of {number} is {rac} and is less than 6 and not 0")
