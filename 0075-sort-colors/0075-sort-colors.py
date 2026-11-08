class Solution:
    def sortColors(self, nums: list[int]) -> None:
        cnt_zero = 0
        cnt_one = 0
        cnt_two = 0

        for ele in nums:
            if ele == 0:
                cnt_zero += 1
            elif ele == 1:
                cnt_one += 1
            else:
                cnt_two += 1
        
        for i in range(len(nums)):
            if cnt_zero:
                nums[i] = 0
                cnt_zero -= 1
            elif cnt_one:
                nums[i] = 1
                cnt_one -= 1
            else:
                nums[i] = 2
                cnt_two -= 1
        