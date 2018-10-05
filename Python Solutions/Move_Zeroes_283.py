# https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        zeroes = 0
        for i in range(len(nums)):
            if nums[i]==0:
                zeroes+=1
            else:
                nums[count] = nums[i]
                count+=1
        
        for i in range(len(nums)-zeroes,len(nums)):
            nums[i] = 0
