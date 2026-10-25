class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = 0
        s2 = 0
        while a or b:
            if a:
                s1 += 1
                a = a & (a - 1)
            if b:
                s2 += 1
                b = b & (b - 1)
        
        return s1 * s2 if s1 >= s2 else s2 // s1
        