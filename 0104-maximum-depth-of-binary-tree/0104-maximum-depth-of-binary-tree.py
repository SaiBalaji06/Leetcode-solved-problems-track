# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        max_dep = float("-inf")
        
        def dfs(root, dep_cnt):
            nonlocal max_dep
            
            if root is None:
                return
            
            max_dep = max(max_dep, dep_cnt)
            
            dfs(root.left, dep_cnt + 1)
            dfs(root.right, dep_cnt + 1)
            
        
        dfs(root, 1)

        return max_dep
        