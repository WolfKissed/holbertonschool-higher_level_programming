#!/usr/bin/python3
def no_c(my_string):
    meow = ""
    for i in my_string:
        if not (i == 'c' or i == 'C'):
            meow += i
    return meow
