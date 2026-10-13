# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root == None:
            return None
        
        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

        # def search(root, val):
        #     if root == None:
        #         return None
            
        #     if root.val == val:
        #         return root
            
        #     if root.val > val:
        #         return search(root.left, val)
        #     else:
        #         return search(root.right, val)
        
        # return search(root, val)
        
        
        # curr = root
        # while curr:
        #     if curr.val == val:
        #         return curr
        #     if curr.val > val:
        #         curr = curr.left
        #     else:
        #         curr = curr.right
        
        # return None
        