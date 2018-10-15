# https://leetcode.com/problems/closest-binary-search-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.closest = None
        self.value = sys.maxsize
    def traverse(self,root,target):
        if root is None:
            return
        if abs(root.val-target)<self.value:
            self.value = abs(root.val-target)
            self.closest = root.val
        if target < root.val:
            if root.left:
                self.traverse(root.left,target)
        else:
            if root.right:
                self.traverse(root.right,target)
            
        
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.traverse(root,target)
        return self.closest
