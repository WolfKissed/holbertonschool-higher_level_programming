#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    x = -1 * number
    n = x % 10
else:
    n = number % 10
if n == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, n))
elif n > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, n))
elif n < 6 and n != 0 :
    print("Last digit of", end="")
    print("{:d} is {:d} and is less than 6 and not 0".format(number, n))
