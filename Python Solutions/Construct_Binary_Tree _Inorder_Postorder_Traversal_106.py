# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

class Solution:
    def generate(self,inorder,postorder,start,end,index):
        if len(postorder)==0:
            return None
        root = TreeNode(postorder.pop())
        i=index[root.val]
        
        root.left = self.generate(inorder,postorder[:i-start],start,i,index)
        root.right = self.generate(inorder,postorder[i-start:],i+1,end,index)
        return root
        
        
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        
        return self.generate(inorder,postorder,0,len(inorder)-1,index)
        
