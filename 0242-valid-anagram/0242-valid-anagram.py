class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        su = 0
        if len(s) == len(t):
            for ele in s:
                if ele not in hm:
                    hm[ele] = 1
                else:
                    hm[ele] += 1
                su += 1
            
            for c in t:
                if c in hm:
                    if hm[c] > 0:
                        hm[c] -= 1
                        su -= 1
            
            if su == 0:
                return True
            return False
        return False
