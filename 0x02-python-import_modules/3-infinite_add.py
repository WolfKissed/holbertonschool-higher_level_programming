        #!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv)
    s = 0
    if x > 1:
        for args in sys.argv:
            if args != sys.argv[0]:
                s = s + int(args)
    print(s)
