#!/usr/bin/python3
#function that removes all characters c and C from a string

def no_c(my_string):
    new_str = [i for i in my_string if i != "c" if i != "C"]
    return "".join(new_str)
