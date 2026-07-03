class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        temp = [[] for _ in range(n)]
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1

        for ky, v in hm.items():
            temp[v - 1].append(ky)
        
        res = []
        for i in range(n - 1, -1, -1):
            p = len(temp[i])
            if p > 0:
                res += temp[i]
                k -= p
                if k == 0:
                    return res

        

        
        