#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    x = 0
    for i in range(n):
        try:
            print(my_list[i], end="")
            x += 1
        except:
            break
    print("")
    return (x)
