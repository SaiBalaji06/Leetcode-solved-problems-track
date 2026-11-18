# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        tree_que = []

        t_que = []
        t_que.append(root)
        t_que.append(-101)

        t = []
        while t_que:
            if t_que[0] != -101:
                if t_que[0] and t_que[0].left:
                    t_que.append(t_que[0].left)
                    t_que[0].left = None
                elif t_que[0] != None:
                    t_que.append(None)
                    
                if t_que[0] and t_que[0].right:
                    t_que.append(t_que[0].right)
                    t_que[0].right = None
                elif t_que[0] != None:
                    t_que.append(None)
                    
                t.append(t_que[0])
                t_que.pop(0)
            else:
                t_que.pop(0)
                if t_que:
                    t_que.append(-101)
                tree_que.append(t)
                t = []
        
        que = []

        root = None
        left_flag = False
        right_flag = False
        for lev in tree_que:
            for i in range(len(lev) - 1, -1, -1):
                if root is None:
                    root = lev[i]
                    que.append(lev[i])
                else:
                    if lev[i] != None:
                        if left_flag == False:
                            que[0].left = lev[i]
                            que.append(lev[i])
                            left_flag = True
                        elif right_flag == False:
                            que[0].right = lev[i]
                            que.append(lev[i])
                            right_flag = True
                    else:
                        if left_flag == False:
                            que[0].left = None
                            left_flag = True
                        elif right_flag == False:
                            que[0].right = None
                            right_flag = True
                
                if left_flag and right_flag:
                    que.pop(0)
                    left_flag = False
                    right_flag = False                    
            
        return root
            



        