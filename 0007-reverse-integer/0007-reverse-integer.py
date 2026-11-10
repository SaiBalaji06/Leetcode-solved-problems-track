class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)
        r = 0
        while n:
            t = n % 10
            r = (r * 10) + t
            n = n // 10

        if x < 0:
            r = r * -1

        if r < -2**31 or r > (2**31) - 1:
            return 0
        
        return r