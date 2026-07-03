class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set(nums)

        if len(hs) == len(nums):
            return False
        return True
        