class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=nums[0]
        for i in range(1,len(nums)):
            result =result^nums[i]
        return result