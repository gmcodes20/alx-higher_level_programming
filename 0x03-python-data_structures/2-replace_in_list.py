#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_lenght = len(my_list)
    if idx < 0 or idx > list_lenght:
        return my_list
    else:
        for val in range(list_lenght):
            if my_list.index(my_list[val]) == idx:
                my_list[val] = element
                return my_list
