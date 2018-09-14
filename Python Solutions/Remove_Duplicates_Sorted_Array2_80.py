# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        flag=0
        while(i<len(nums)):
            if flag==1 and i+1<len(nums) and nums[i]==nums[i+1]:
                nums.pop(i+1)
            elif flag==0 and i+1<len(nums) and nums[i]==nums[i+1] :
                i+=1
                flag=1
            else:
                i+=1
                flag=0
                
        return len(nums)
        
