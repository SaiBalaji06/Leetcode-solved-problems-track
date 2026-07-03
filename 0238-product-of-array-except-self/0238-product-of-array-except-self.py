class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        sufix_product = [1]
        n = len(nums)
        for i in range(n):
            prefix_product.append(prefix_product[i] * nums[i])
            sufix_product.append(sufix_product[i] * nums[n - i - 1])
        res = []
        for j in range(n):
            res.append(prefix_product[j] * sufix_product[n - j - 1])

        return res