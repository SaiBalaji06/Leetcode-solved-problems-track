# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head

        if head:
            while ptr2:
                if ptr1 != ptr2 and ptr1.val != ptr2.val:
                    ptr1.next = ptr2
                    ptr1 = ptr1.next
                ptr2 = ptr2.next

            ptr1.next = None

        return head
        