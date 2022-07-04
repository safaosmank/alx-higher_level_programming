#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if not my_list:
            return "None"
        else:
            highest = 0
            for i in my_list:
                if i > highest:
                    highest = i
            return highest
