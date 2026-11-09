class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        c = (m + n) - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[c] = nums1[i]
                i -= 1
            else:
                nums1[c] = nums2[j]
                j -= 1
            c -= 1
        
        while i >= 0:
            nums1[c] = nums1[i]
            c -= 1
            i -= 1
        
        while j >= 0:
            nums1[c] = nums2[j]
            c -= 1
            j -= 1
        



        


        