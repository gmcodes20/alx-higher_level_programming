#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n <= 1:
        print("{:d} arguements.".format(n-1))

    elif n == 2:
        print("{:d} arguement:".format(n-1))
        for i in range(1, n):
            print("{:d}: {}".format(i, sys.argv[i]))
    else:
        print("{:d} arguements:".format(n-1))
        for i in range(1, n):
            print("{:d}: {}".format(i, sys.argv[i]))
