# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        mx = nums[0]
        for i in range(len(nums)):
            if nums[i]!=0:
                p = p*nums[i]
                if p>mx:
                    mx=p
            else:
                p=1
                if mx<0:
                    mx=0      
        p=1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=0:
                p = p*nums[i]
                if p>mx:
                    mx=p
            else:
                p=1
                if mx<0:
                    mx=0
            
        return mx
        
