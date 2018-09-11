class Solution:
    def doRob(self,nums):
        x = [0 for i in nums]
        x[0] = nums[0]
        x[1] = nums[1] if nums[1]>nums[0] else nums[0]
        for i in range(0,len(nums)):
            if i>1:
                x[i] = max(x[i-1],x[i-2]+nums[i])
        return x[len(nums)-1]
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            v1 = self.doRob(nums[:len(nums)-1])
            v2 = self.doRob(nums[1:])
            return max(v1,v2)