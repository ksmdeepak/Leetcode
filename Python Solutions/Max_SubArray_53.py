class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumSoFar = 0
        m=0
        mn = -sys.maxint - 1 
        count=0
        
        for i in range(0,len(nums)):
            if nums[i]<0:
                count+=1
            sumSoFar = sumSoFar+nums[i]
            if sumSoFar>m:
                m=sumSoFar
            if sumSoFar<0:
                if sumSoFar > mn:
                    mn = sumSoFar
                sumSoFar = 0
        if count==len(nums):
            return mn
        return m
                
            