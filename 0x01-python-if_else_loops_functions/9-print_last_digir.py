#!/usr/bin/python3
def print_last_digit(number):
    i = number % 10
    if number > 0:
        i = number % 10
    elif number < 0:
        i = abs(number) % 10
    print(i, end="")
    return i
