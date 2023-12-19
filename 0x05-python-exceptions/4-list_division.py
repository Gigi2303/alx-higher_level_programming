#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    ley = []
    for g in range(list_length):
        result = 0
        try:
            result = my_list_1[g] / my_list_2[g]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new.append(result)
    return ley
