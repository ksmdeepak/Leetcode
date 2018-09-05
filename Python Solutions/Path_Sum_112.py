# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkPath(self,root,sum):
        if root is None:
            return False
        if root.left is None and root.right is None and sum-root.val==0 :
            return True
        else:
            return self.checkPath(root.left,sum-root.val) or self.checkPath(root.right,sum-root.val)
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        else:
            return self.checkPath(root,sum)
        
    