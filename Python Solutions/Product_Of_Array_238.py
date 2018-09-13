class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        productSoFar = 1
        output = []
        for i in range(len(nums)):
            output.append(productSoFar)
            productSoFar*= nums[i]
        productSoFar=1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=productSoFar
            productSoFar*=nums[i]
        return output