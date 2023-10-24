#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    product = []

    for i in range(list_length):
        try:
            et1 = my_list_1[i]
            et2 = my_list_2[i]

            if isinstance(et1, (int, float)) and isinstance(et2, (int, float)):
                if et2 == 0:
                    raise ZeroDivisionError
                result = et1 / et2
            else:
                raise TypeError

        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            product.append(division_result)

    return product
