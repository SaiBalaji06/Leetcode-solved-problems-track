class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        pi = nums[0] - 1
        for i in range(n - 2):
            if nums[i] != pi:
                j = i + 1
                k = n - 1
                pj = nums[j] - 1
                pk = nums[k] - 1
                trg = 0 - nums[i]
                while k > j:
                    if nums[j] != pj:
                        if nums[j] + nums[k] == trg:
                            ans.append([nums[i], nums[j], nums[k]])
                            pj = nums[j]
                            pk = nums[k]
                            j += 1
                            k -= 1
                        else:
                            if nums[j] + nums[k] > trg:
                                pk = nums[k]
                                k -= 1
                            else:
                                pj = nums[j]
                                j += 1
                    else:
                        if pj == nums[j]:
                            pj = nums[j]
                            j += 1
                        if pk == nums[k]:
                            pk = nums[k]
                            k -= 1
                pi = nums[i]
                
        return ans
                
                
