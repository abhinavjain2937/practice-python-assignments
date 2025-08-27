def int_to_roman(num):
    val_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = ""
    num = int(num)  # Convert string to integer

    for val, roman in val_to_roman:
        while num >= val:
            result += roman
            num -= val

    return result

# Example usage
num = '5268'
print(int_to_roman(num))  # Output: MMDCCLXVIII


