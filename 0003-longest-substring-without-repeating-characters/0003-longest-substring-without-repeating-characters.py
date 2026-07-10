class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hs = set()
        l = 0
        res = 0

        for r in range(n):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1

            hs.add(s[r])
            res = max(res, r - l + 1)

        return res







        # res = 0
        # for i in range(n):
        #     cnt = 0
        #     hs = set()
        #     for j in range(i, n):
        #         if s[j] not in hs:
        #             cnt += 1
        #             hs.add(s[j])
        #         else:
        #             break
        #     res = max(res, cnt)
        
        # return res


                

        