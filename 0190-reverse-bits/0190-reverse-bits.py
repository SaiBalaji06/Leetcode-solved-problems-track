class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(31):
            t = n & 1
            res = res ^ t

            n = n >> 1
            res = res << 1
        
        return res