class Solution:
    def romanToInt(self, s: str) -> int:
        RHM = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        roman_int = 0

        for ch in s:
            roman_int += RHM[ch]
        
        roman_sub = 0
        for i in range(len(s) - 1):
            if s[i] == 'I':
                if s[i + 1] == 'V' or s[i + 1] == 'X':
                    roman_sub += RHM['I']
            elif s[i] == 'X':
                if s[i + 1] == 'L' or s[i + 1] == 'C':
                    roman_sub += RHM['X']
            elif s[i] == 'C':
                if s[i + 1] == 'D' or s[i + 1] == 'M':
                    roman_sub += RHM['C']
        
        roman_int -= (roman_sub * 2)
        
        return roman_int


        