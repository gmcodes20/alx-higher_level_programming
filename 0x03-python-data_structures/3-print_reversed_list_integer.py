#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        list_size = len(my_list)
        for item in (range(-1, -list_size - 1, -1)):
            print("{}".format(my_list[item]))
