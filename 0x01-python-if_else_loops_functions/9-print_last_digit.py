#!/usr/bin/python3
def print_last_digit(number):
    my_number = number % 10
    print("{:1}".format(my_number))
    return my_number
