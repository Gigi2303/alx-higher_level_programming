#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    product, avg = 0, 0

    for g in my_list:
        calc = g[0] * g[1]
        product += calc
        avg += g[1]
    weight = product / avg
    return weight
