# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        q1 = []
        q2 = []
        output=[]
        if root is None:
            return []
        else:
            q1.append(root)
            level = []
            while(len(q1)!=0 or len(q2)!=0): 
                a = q1 if len(q1)>0 else q2
                b = q1 if len(q2) >0 else q2
                while(len(a)>0):
                    temp = a.pop(0)
                    level.append(temp.val)
                    if temp.left:
                        b.append(temp.left)
                    if temp.right:
                        b.append(temp.right)
                output.append(level.copy())
                level=[]
        return output
            