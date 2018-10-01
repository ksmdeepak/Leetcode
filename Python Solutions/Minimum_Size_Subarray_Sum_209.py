#

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        sumSoFar = 0
        length = len(nums)+1
        while i<len(nums) and j<len(nums):     
            sumSoFar+= nums[j]       
            while sumSoFar >= s:
                length = min(j-i+1,length)
                sumSoFar-=nums[i]
                i+=1             
            j+=1
        if length != len(nums)+1:
            return length
        else:
            return 0
        
        
