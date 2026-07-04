class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mi = float("inf")

        while(high >= low):
            mid = low + (high - low) // 2
            if nums[high] > nums[low] and nums[mid] > nums[low]:
                mi = min(mi, nums[low])
                high = mid - 1
            elif nums[low] > nums[high] and nums[mid] > nums[high]:
                mi = min(mi, nums[high])
                low = mid + 1
            else:
                mi = min(mi, nums[mid])
                high = mid - 1
        
        return mi

        # while(high > low):
        #     mid = low + (high - low) // 2
        #     if nums[mid] > nums[high]:
        #         low = mid + 1
        #     else:
        #         high = mid
        
        # return nums[low]
            


            

        