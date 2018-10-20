# https://leetcode.com/problems/k-empty-slots/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def addNode(self,root,node):
        mn=mx=-1
        temp=root
        while temp:
            if node.val<temp.val:
                if mx==-1 or temp.val<mx:
                    mx=temp.val
                if temp.left:
                    temp=temp.left
                else:
                    temp.left=node
                    return (mn,mx)
            else:
                if mn==-1 or temp.val>mn:
                    mn=temp.val
                if temp.right:
                    temp=temp.right
                else:
                    temp.right=node
                    return (mn,mx)
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if len(flowers)<=2:
            if k==0:
                return 2
            else:
                return -1
        else:
            root = TreeNode(flowers[0])
            for i in range(1,len(flowers)):
                node = TreeNode(flowers[i])
                mn,mx = self.addNode(root,node)
                if (mx!=-1 and mx-flowers[i]==k+1) or (mn!=-1 and flowers[i]-mn==k+1):
                    return i+1
        return -1
                
        
