# https://leetcode.com/problems/valid-perfect-square/description/

class Solution(object):
    def binarySearch(self,l,r,target):
        if l<=r:
            
            mid = int((l+r)/2)
            print(mid)
            value = mid**2
            if value==target:
                return True
            else:
                if value>target:
                    return self.binarySearch(l,mid-1,target)
                else:
                    return self.binarySearch(mid+1,r,target)
        
        return False
        
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        return self.binarySearch(1,num,num)
