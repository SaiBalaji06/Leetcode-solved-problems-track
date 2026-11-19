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
        
        def dfs_maxdepth(root):
            if root is None:
                return 0
            
            left = dfs_maxdepth(root.left)
            right = dfs_maxdepth(root.right)

            return max(left, right) + 1
        
        # max_dep = float("-inf")
        
        # def dfs(root, dep_cnt):
        #     nonlocal max_dep
            
        #     if root is None:
        #         return
            
        #     max_dep = max(max_dep, dep_cnt)
            
        #     dfs(root.left, dep_cnt + 1)
        #     dfs(root.right, dep_cnt + 1)
            
        
        return dfs_maxdepth(root)
        