#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    x = len(my_list)
    if idx > (x - 1):
        return (None)
    return (my_list[idx])
