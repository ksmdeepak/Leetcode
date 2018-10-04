# https://leetcode.com/problems/first-bad-version/description/

class Solution(object):
    def binarySearch(self,l,r):
        if l<=r:
            mid = int((l+r)/2)       
            valid = isBadVersion(mid)
            if valid and mid>0 and not isBadVersion(mid-1) :
                return mid
            elif valid:
                return self.binarySearch(l,mid-1)
            else:
                return self.binarySearch(mid+1,r)
        return -1
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarySearch(1,n)
