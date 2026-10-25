class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(" ")
        res = 0

        i = len(s) - 1

        while i != -1 and s[i] != " ":
            res += 1
            i -= 1

        return res
        