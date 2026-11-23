# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def dfs_tree(p, q):
            if not p and not q:
                return True
            
            if (p and q == None) or (p == None and q):
                return False
                
            if p.val != q.val:
                return False
            
            left = dfs_tree(p.left, q.left)
            right = dfs_tree(p.right, q.right)

            return left and right
        
        return dfs_tree(p, q)
            




        # def dfs_tree(root, sta):
        #     if root is None:
        #         return 
            
        #     dfs_tree(root.left, sta)
        #     dfs_tree(root.right, sta)

        #     if sta == 1:
        #         if root.left or root.right:
        #             if root.left:
        #                 res1.append(root.left.val)
        #             else:
        #                 res1.append(None)
        #             if root.right:
        #                 res1.append(root.right.val)
        #             else:
        #                 res1.append(None)
        #     elif sta == 2:
        #         if root.left or root.right:
        #             if root.left:
        #                 res2.append(root.left.val)
        #             else:
        #                 res2.append(None)
        #             if root.right:
        #                 res2.append(root.right.val)
        #             else:
        #                 res2.append(None)
        
        # res1 = []

        # dfs_tree(p, sta = 1)
        # if p:
        #     res1.append(p.val)


        # res2 = []

        # dfs_tree(q, sta = 2)
        # if q:
        #     res2.append(q.val)

        # return res1 == res2
        
        