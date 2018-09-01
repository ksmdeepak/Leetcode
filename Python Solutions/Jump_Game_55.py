class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length=len(nums)
        if length==0:
            return True;
        elif length==1:
            return True;
        
        positionReach = length-1
        for i in range(length-1,-1,-1):
            print(i)
            if(nums[i]+i>=positionReach):
                positionReach = i
        return positionReach==i