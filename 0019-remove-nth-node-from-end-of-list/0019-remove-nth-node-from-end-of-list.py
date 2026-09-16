# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        len_list = 0
        t = head

        while t:
            len_list += 1
            t = t.next
        
        n = (len_list - n) + 1

        curr = head
        pre = None
        curr_len = 1

        if n == 1:
            head = head.next
        else:
            while curr_len != n:
                pre = curr
                curr = curr.next
                curr_len += 1
            pre.next = curr.next
            curr.next = None
        
        return head
        