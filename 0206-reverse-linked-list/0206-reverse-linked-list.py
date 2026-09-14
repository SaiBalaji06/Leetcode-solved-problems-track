# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        Next = None
        pre = None

        while curr:
            Next = curr.next
            curr.next = pre
            pre = curr
            curr = Next
        
        return pre

        