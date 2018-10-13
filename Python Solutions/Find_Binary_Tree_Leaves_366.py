# https://leetcode.com/problems/find-leaves-of-binary-tree/description/

class Solution(object):
    def __init__(self):
        self.output=[]
    def height(self,root):
        if root is None:
            return -1
        else:
            l = self.height(root.left)
            r = self.height(root.right)
            height = 1 + max(l,r)
            if len(self.output)<height+1:
                self.output.append([])
            self.output[height].append(root.val)
            return height
                
        
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.height(root)
        return self.output
        
