class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        hm = {}
        uni = 0

        i = 0
        j = 0
        mx = 0
        while j < n:
            if uni <= 2:
                if fruits[j] not in hm:
                    hm[fruits[j]] = 1
                    uni += 1
                else:
                    hm[fruits[j]] += 1
                if uni <= 2:
                    mx = max(mx, j - i + 1)
                j += 1
            else:
                hm[fruits[i]] -= 1
                if hm[fruits[i]] == 0:
                    del hm[fruits[i]]
                    uni -= 1
                i += 1
        return mx
            

        