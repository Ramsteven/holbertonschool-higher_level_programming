#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    result = 0
    if len(roman_string) == 1:
        return dic[roman_string[0]]
    for i in range(0, len(roman_string)):
        if i == len(roman_string) - 1:
            result += dic[roman_string[i]]
            return result
        if dic[roman_string[i]] >= dic[roman_string[i + 1]]:
            result += dic[roman_string[i]]
        elif dic[roman_string[i]] < dic[roman_string[i + 1]]:
            result += dic[roman_string[i + 1]] - dic[roman_string[i]]
            if (i + 2 <= len(roman_string)):
                    i += 2
            else:
                return result
