#!/usr/bin/python3

def to_subtract(list_num):
    sub_val = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            sub_val += n

    return (max_list - sub_val)

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    idx = 0
    l_fig = 0
    list_num = [0]

    for chars in roman_string:
        for r_num in list_keys:
            if r_num == chars:
                if rom_n.get(chars) <= l_fig:
                    idx += to_subtract(list_num)
                    list_num = [rom_n.get(chars)]
                else:
                    list_num.append(rom_n.get(chars))

                l_fig = rom_n.get(chars)
    idx += to_subtract(list_num)
    return (idx)

