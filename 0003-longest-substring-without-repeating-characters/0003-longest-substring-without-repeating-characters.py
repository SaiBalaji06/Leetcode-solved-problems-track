class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            cnt = 0
            hs = set()
            for j in range(i, n):
                if s[j] not in hs:
                    cnt += 1
                    hs.add(s[j])
                else:
                    break
            res = max(res, cnt)
        
        return res
                

        