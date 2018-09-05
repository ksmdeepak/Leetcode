# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self,root,output):
        if root is None:
            return
        self.traverse(root.left,output)
        output.append(root.val)
        self.traverse(root.right,output)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output= []
        self.traverse(root,output);
        return output
        
        