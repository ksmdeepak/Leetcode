# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=1:
            return 0
        start = 0
        count = 0
        productSoFar = 1
        for end in range(len(nums)):
            productSoFar*= nums[end]
            while productSoFar>=k:
                productSoFar=productSoFar/nums[start]
                start+=1
            count+=(end-start+1)
        return count
        
        
        
                
