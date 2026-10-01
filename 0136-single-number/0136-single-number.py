class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0

        for ele in nums:
            res = res ^ ele
        
        return res
        