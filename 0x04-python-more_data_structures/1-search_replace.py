#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda value: replace
                    if value == search else value, my_list))
