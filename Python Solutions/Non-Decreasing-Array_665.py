# https://leetcode.com/problems/non-decreasing-array/description/

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        nums = [-1]+nums
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1]:
                continue
            else:
                if count>=1:
                    return False
                if nums[i]< nums[i-2]:
                    nums[i]=nums[i-1]
                count+=1
        return True
