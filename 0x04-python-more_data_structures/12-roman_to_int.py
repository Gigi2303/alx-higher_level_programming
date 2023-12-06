#!/usr/bin/python3

def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return 0
    result = 0

    zip_string = zip(roman_string, roman_string[1:])

    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for g, b in zip_string:
        if g not in dic.keys():
            return 0
        elif dic[g] >= roman_dic[b]:
            result += roman_dic[g]
        else:
            result -= roman_dic[g]
    result += roman_dic[roman_string[-1]]
    return (result)
