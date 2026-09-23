# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if head.next:
            temp = head

            slowptr = head
            fastptr = head
            pre = None

            while fastptr and fastptr.next:
                pre = slowptr
                slowptr = slowptr.next
                fastptr = fastptr.next.next
            
            pre.next = None

            curr = slowptr
            nextptr = None
            preptr = None

            while curr:
                nextptr = curr.next
                curr.next = preptr
                preptr = curr
                curr = nextptr

            ptr1 = head
            t1 = ptr1.next

            ptr2 = preptr
            t2 = ptr2.next

            while t1:
                ptr2.next = None
                ptr1.next = ptr2
                ptr1.next.next = t1
                ptr1 = t1
                t1 = t1.next
                ptr2 = t2
                if t2:
                    t2 = t2.next
            
            if ptr2:
                ptr1.next = ptr2

        