class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1 or len(s) > 15:
            return -1
        roman_conv_int = 0
        roman_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for letter in s:
            if letter in roman_int_dict:
                roman_conv_int = roman_conv_int + roman_int_dict.get(letter)
            else:
                return -1
        return roman_conv_int
