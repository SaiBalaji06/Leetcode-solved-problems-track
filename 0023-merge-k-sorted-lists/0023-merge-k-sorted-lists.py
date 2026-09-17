# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        def merge(left, right):
            templist = ListNode()
            t1 = templist

            l1 = left
            l2 = right

            while l1 and l2:
                if l1.val > l2.val:
                    t1.next = l2
                    l2 = l2.next
                else:
                    t1.next = l1
                    l1 = l1.next
                t1 = t1.next
            
            if l1:
                t1.next = l1
            if l2:
                t1.next = l2
            
            return templist.next
            


        low = 0
        high = len(lists) - 1
        def dividelist(low, high):
            if high - low == 0:
                return lists[low]

            mid = low + (high - low) // 2

            left = dividelist(low, mid)
            right = dividelist(mid + 1, high)

            return merge(left, right)

        return dividelist(low, high)
