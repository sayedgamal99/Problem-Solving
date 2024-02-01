class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        for i in range(len(s)-1):
            if roman_numerals_map[s[i]]>=roman_numerals_map[s[i+1]]: #VI
                result+=roman_numerals_map[s[i]]
            else:
                result-=roman_numerals_map[s[i]]

        return result+roman_numerals_map[s[-1]]