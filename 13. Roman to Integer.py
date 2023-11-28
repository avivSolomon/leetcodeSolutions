ROMAN_DIG ={'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

class Solution:
    def romanToInt(self, roman_number: str) -> int:
        trans = 0
        i = 0
        while i < len(roman_number):
            if i + 1 < len(roman_number):
                if ROMAN_DIG[roman_number[i]] < ROMAN_DIG[roman_number[i+1]]:
                    trans = trans - ROMAN_DIG[roman_number[i]]
                else:
                    trans = trans + ROMAN_DIG[roman_number[i]]
            else:
                trans = trans + ROMAN_DIG[roman_number[-1]]
            i += 1
        return trans

# print(trans_roman_to_int(input('enter romans dig:')))

