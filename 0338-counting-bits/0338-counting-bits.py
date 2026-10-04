class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            a = i
            while i:
                i = i & (i - 1)
                res[a] += 1
        
        return res
        