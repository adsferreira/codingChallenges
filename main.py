from roman_to_integer import Solution


if __name__ == '__main__':
    roman_nr = 'LVIII'
    roman_converted_int = Solution().romanToInt(roman_nr)
    print(f'The roman number {roman_nr} converted to integer is {roman_converted_int}.')
