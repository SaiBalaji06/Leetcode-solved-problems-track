class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # def minval(nums, n):
        #     left = 0
        #     right = n - 1

        #     while(right > left):
        #         mid = left + (right - left) // 2

        #         if nums[mid] > nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid
        #     return left
        
        # n = len(nums)
        # miind = minval(nums, n)
        
        # low = 0
        # high = n - 1

        # while(high >= low):
        #     mid = low + (high - low) // 2
        #     t = (miind + mid) % n

        #     if(nums[t] == target):
        #         return t

        #     if(nums[t] > target):
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        
        # return -1

        low = 0
        high = len(nums) - 1

        while(high >= low):
            mid = low + (high - low) // 2
            if(nums[mid] == target):
                return mid
            
            if(nums[low] <= nums[mid]):
                if(target >= nums[low] and nums[mid] >= target):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if(target >= nums[mid] and nums[high] >= target):
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1

        
    

        