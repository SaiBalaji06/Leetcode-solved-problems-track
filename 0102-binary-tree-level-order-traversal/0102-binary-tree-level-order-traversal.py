# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        res = []

        que = []
        que.append(root)
        que.append(1001)

        t = []
        while que:
            if que[0] != 1001:
                if que[0].left:
                    que.append(que[0].left)
                if que[0].right:
                    que.append(que[0].right)
                
                t.append(que[0].val)
                que.pop(0)
            else:
                res.append(t)
                t = []
                que.pop(0)
                if que:
                    que.append(1001)
        
        return res
            
        