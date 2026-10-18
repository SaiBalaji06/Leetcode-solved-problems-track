# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        def inorder(root, reslst):
            if root == None:
                return reslst
            inorder(root.left, reslst)
            reslst.append(root.val)
            inorder(root.right, reslst)
        
        reslst = []
        inorder(root, reslst)
        
        return reslst
        