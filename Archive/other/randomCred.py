"""
Name: Gabriel Engberg
Date: 14-02-2022
Info:
A program that generate n amount of names and phone number if wanted.
Returns a dict with names as key and phone number as value or None if phone number is not opted for.
"""
from names import get_full_name
from random import randint


def get_persons(n: int = 1, gen_phone: bool = True):
    # Function to generate a random phone number with prefix "07"
    def gen_number():
        # Example: "072 445 66 23"
        out = "07"
        for _ in range(8):
            out = out + str(randint(0, 9))
        # adds spaces => "0701234567" => "070 123 45 67"
        return out[:3] + " " + out[3:6] + " " + out[6:8] + " " + out[8:10]

    # Generate names...
    listOfPeople = {}
    for i in range(n):
        listOfPeople[get_full_name()] = gen_number() if gen_phone else None

    return listOfPeople
