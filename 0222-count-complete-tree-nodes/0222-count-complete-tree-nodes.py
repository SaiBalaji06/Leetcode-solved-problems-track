# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
            
        if root.left is None and root.right is None:
            return 1
            
        curr_left = root
        curr_right = root
        lefthei = 0
        righthei = 0

        while curr_left or curr_right:
            if curr_left:
                lefthei += 1
                curr_left = curr_left.left
            if curr_right:
                righthei += 1
                curr_right = curr_right.right
        
        res = (1 << max(lefthei, righthei)) - 1

        if lefthei == righthei:
            return res

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        