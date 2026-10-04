class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False

        c = 0
        while n:
            if n & 1 == 1:
                c += 1
            n = n >> 1
        
        if c == 1:
            return True
        return False

        