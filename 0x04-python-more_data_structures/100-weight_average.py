#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    suma = 0
    secon_sum = 0
    for i in my_list:
        mul = 1
        n = 0
        for y in i:
            mul *= y
            n += 1
            if n == 2:
                secon_sum += y
        suma += mul

    return suma/secon_sum
