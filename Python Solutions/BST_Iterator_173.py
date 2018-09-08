# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        x = root
        
        while x is not None:
            self.stack.append(x)
            x = x.left
           
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack)!=0:
            return True
        else:
            return False
        

    def next(self):
        """
        :rtype: int
        """ 
        temp = self.stack[len(self.stack)-1]
        self.stack.pop()
        if temp.right:
            x = temp.right
            while x is not None:
                self.stack.append(x)
                x = x.left
        return temp.val


        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())