# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.mx = -sys.maxint-1
    def findMaxSumPath(self,root):
        if root is None:
            return 0
        else:
            l = self.findMaxSumPath(root.left)
            r = self.findMaxSumPath(root.right)       
            l = l if l>0 else 0
            r = r if r>0 else 0
            value = l if l>r else r 
            sum = root.val+l+r
            if sum>self.mx:
                self.mx = sum      
            return root.val+value
            
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.findMaxSumPath(root)
        return self.mx
        