
"""
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV, because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a an integer, convert it to Roman numeral.
"""
def int_to_Roman(num):
    """
    Given an integer, convert it to a roman numberal
    """
    # list of the interger convert to a roman numberal 
    values_integer = [1000, 900,  500, 400,  100,  90,   50, 40,   10,   9,    5,   4,   1]
    values_roman =   [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    # string contain the roman numberal
    roman_num = ''
    # value runs from largest to smallest of the array
    i = 0
    while  num > 0:
        # divide number by the value from largest to smallest in values_integer
        for x in range(num // values_integer[i]):
            # add the value of the roman numeral corresponding to the integer divisor
            roman_num += values_roman[i]
            # and number sub the integer divisor
            num -= values_integer[i]
        i += 1
    return roman_num
# input the number
num = int(input('num = '))
# convert the number to roman numberal
print(int_to_Roman(num))

