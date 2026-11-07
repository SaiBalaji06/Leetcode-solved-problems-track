class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = {'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)
        i = 0
        j = len(s) - 1

        while j >= i:
            if (s[i] in vow) and (s[j] in vow):
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            else:
                if s[i] not in vow:
                    i += 1
                if s[j] not in vow:
                    j -= 1
        
        return "".join(s)


        