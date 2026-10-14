class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = nums[0]
        currmax = nums[0]
        globalmax = nums[0]
        n = len(nums)
        i = 1
        while i < n:
            if nums[i] + currsum > nums[i]:
                currsum += nums[i]
            else:
                currsum = nums[i]
            
            currmax = max(currmax, currsum)
            globalmax = max(globalmax, currmax)
            
            i += 1


        return globalmax