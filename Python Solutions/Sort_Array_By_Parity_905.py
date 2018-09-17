# https://leetcode.com/problems/sort-array-by-parity/description/

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i=0
        j=len(A)-1
        while i<j and j>=0 and i<len(A):
            while i<len(A) and A[i]%2==0:
                i+=1
            while j>=0 and A[j]%2==1:
                j-=1
            if i<j:
                A[i],A[j] = A[j],A[i]
                i+=1
                j-=1
        return A
        
