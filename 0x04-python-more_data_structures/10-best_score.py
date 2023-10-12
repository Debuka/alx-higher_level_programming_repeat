#!/usr/bin/python3

"""this return the key with the biggest int value"""
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
