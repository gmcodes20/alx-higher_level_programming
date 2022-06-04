#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_own_list = my_list[:]
    list_lenght = len(my_list)
    if idx < 0:
        return my_list
    if idx > list_lenght:
        return my_list
    for val in range(list_lenght):
        if my_list.index(my_list[val]) == idx:
            my_own_list[val] = element
            return my_own_list
