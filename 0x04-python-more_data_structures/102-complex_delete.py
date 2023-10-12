#!/usr/bin/python3

"""deletes keys with a specific value fro th list"""
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for val_dictionary in list_keys:
        if value == a_dictionary.get(val_dictionary):
            del a_dictionary[val_dictionary]

    return (a_dictionary)
