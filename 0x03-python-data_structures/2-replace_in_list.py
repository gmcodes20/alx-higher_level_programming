#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_lenght = len(my_list)
    if idx < 0 or idx > list_lenght:
        return my_list
    else:
        my_list[idx] = element
        return my_list
