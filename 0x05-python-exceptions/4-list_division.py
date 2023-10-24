#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            element1 = my_list_1[i]
            element2 = my_list_2[i]

            if isinstance(element1, (int, float)) and isinstance(element2, (int, float)):
                if element2 == 0:
                    raise ZeroDivisionError
                division_result = element1 / element2
            else:
                raise TypeError

        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except TypeError:
            print("wrong type")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            result.append(division_result)

    return result
