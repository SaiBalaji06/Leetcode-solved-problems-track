# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if (root is None) or (subRoot is None):
            return False
        
        res = False
        if root.val == subRoot.val:
            res = self.match_subtree(root, subRoot)
            
        if res:
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right

    def match_subtree(self, root, subRoot):
        if (root is None) and (subRoot is None):
            return True
        
        if ((root is None) and subRoot) or (root and (subRoot is None)):
            return False
        
        if root.val != subRoot.val:
            return False
        
        left = self.match_subtree(root.left, subRoot.left)
        right = self.match_subtree(root.right, subRoot.right)
        return left and right

        # def dfs_subtree(root, subRoot):
        #     if (root is None) or (subRoot is None):
        #         return False
            
        #     res = False
        #     if root.val == subRoot.val:
        #         res = match_subtree(root, subRoot)
                
        #     if res:
        #         return True
            
        #     left = dfs_subtree(root.left, subRoot)
        #     right = dfs_subtree(root.right, subRoot)
        #     return left or right
        
        # return dfs_subtree(root, subRoot)


        