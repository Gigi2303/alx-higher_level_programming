#!/usr/bin/python3

def fizzbuzz():
    for g in range(1, 101):
        if g % 3 == 0 and g % 5 == 0:
            print("FizzBuzz", end=" ")
        elif g % 3 == 0:
            print("Fizz", end=" ")
        elif g % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(g, end=" ")
