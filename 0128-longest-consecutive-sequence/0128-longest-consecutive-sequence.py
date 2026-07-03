class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        nums = set(nums)
        gm = float("-inf")
        for ele in nums:
            if ele - 1 not in nums:
                cn = 1
                ele = ele + 1
                while ele in nums:
                    cn += 1
                    ele += 1
                gm = max(gm, cn)
        return gm