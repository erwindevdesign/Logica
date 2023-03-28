def intToRoman(num: int) -> str:
    roman_num = ""
    roman_mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    for value, symbol in roman_mapping:
        #print(f"for value: {value}, symbol: {symbol} ")
        while num >= value:
            print(f"while num: {num} >= value: {value}")
            roman_num += symbol
            num -= value
    return roman_num
    
print(intToRoman(2))
#print(intToRoman(52))
#print(intToRoman(255))