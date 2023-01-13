#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        sum_roma = 0
        num = 0
        ant = 0
        rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for letter in reversed(roman_string):
            num = rom[letter]
            num = num if num >= ant else -num
            sum_roma += num
            ant = num
        return (sum_roma)
    return 0
