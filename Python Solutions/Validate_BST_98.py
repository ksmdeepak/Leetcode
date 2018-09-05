# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def valid(self,root,left,right):
        if root is None:
            return True
        if root.val>left and root.val<right:
            return self.valid(root.left,left,root.val) and self.valid(root.right,root.val,right)
        else:
            return False
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        maxValue = sys.maxint
        minValue = -1*maxValue-1
        return self.valid(root,minValue,maxValue)