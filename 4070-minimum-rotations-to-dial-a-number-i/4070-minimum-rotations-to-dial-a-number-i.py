class Solution:
    def minRotations(self, s: str) -> int:
        pre = 0
        result = 0

        for d in s:
            d = int(d)
            if pre > d:
                backward = abs(pre - d)
                forward = abs(9 - pre) + abs(d - 0) + 1
            else:
                backward = abs(pre - 0) + abs(9 - d) + 1
                forward = abs(pre - d)
                
            result += min(forward, backward)
            pre = d
        
        return result
        
            
        