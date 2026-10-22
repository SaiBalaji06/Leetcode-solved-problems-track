class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while j > i:
            temp = numbers[i] + numbers[j]
            if temp == target:
                return [i + 1, j + 1]
            if temp > target:
                j -= 1
            else:
                i += 1
        


        