# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def binarySearch(self,x,l,r):
        if l<=r:
            mid = int((r+l)/2)
            print(mid)
            if mid*mid==x:
                return mid
            elif (mid+1)*(mid+1)==x:
                return mid+1
            elif mid*mid < x and (mid+1)*(mid+1)>x:
                return mid
            elif mid*mid>x:
                return self.binarySearch(x,l,mid)
            else:
                return self.binarySearch(x,mid+1,r)
        return -1
        
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x in [0,1]:
            return x
        return self.binarySearch(x,1,x)
        
