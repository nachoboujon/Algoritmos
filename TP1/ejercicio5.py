def rumano_a_decimal(roman_numeral):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(roman_numeral) == 0:
        return 0
    elif len(roman_numeral) == 1:
        return roman_numerals[roman_numeral]

    if roman_numerals[roman_numeral[0]] < roman_numerals[roman_numeral[1]]:
        return roman_numerals[roman_numeral[1]] - roman_numerals[roman_numeral[0]] + rumano_a_decimal(roman_numeral[2:])
    else:
        return roman_numerals[roman_numeral[0]] + rumano_a_decimal(roman_numeral[1:])


print(rumano_a_decimal("IV"))  
print(rumano_a_decimal("IX"))  
print(rumano_a_decimal("LVIII"))  
print(rumano_a_decimal("MCMXCIV"))  
