#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastd = number % -10
else:
    lastd = number % 10
    print(f"Last digit of {number} is ")
if lastd > 5:
    print(f"{lastd} and is greater than 5")
elif lastd == 0:
    print(f"{lastd} and is 0")
elif lastd < 6 and lastd != 0:
    print(f"{lastd} and is less than 6 and not 0")
