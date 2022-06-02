#!/usr/bin/python3
def islower(c):
    for i in (range(ord('a') and ord('Z'))):
        if ord(c) > 64 and ord(c) < 91:
            return True
        else:
            return False
