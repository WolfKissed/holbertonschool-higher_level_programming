#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv)
    sum = 0
    if x > 1:
        for args in sys.argv:
            if args != sys.argv[0]:
                sum = sum + int(args)
    print(sum)
