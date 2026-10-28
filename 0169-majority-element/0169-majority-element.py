class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hm = {}
        for ele in nums:
            if ele in hm:
                hm[ele] += 1
            else:
                hm[ele] = 1
        
        for i in nums:
            if hm[i] > (len(nums) // 2):
                return i
        