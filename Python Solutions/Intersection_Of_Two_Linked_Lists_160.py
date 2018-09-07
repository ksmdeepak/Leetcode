class Solution(object):
    def findPivot(self,nums,l,r):
        if(l<=r):
            mid = int((r+l)/2)
            if mid==0 and nums[mid]<nums[mid+1]:
                return mid
            elif mid ==len(nums)-1 and nums[mid]<nums[mid-1]:
                return mid
            elif nums[mid]< nums[mid-1] and nums[mid]<nums[mid+1]:
                return mid
            else:           
                if nums[mid]>=nums[len(nums)-1]:

                    return self.findPivot(nums,mid+1,r)
                else:
                    return self.findPivot(nums,l,mid-1)
        return -1
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==1:
            return nums[0]
        
        pivot=self.findPivot(nums,0,len(nums)-1)
        return nums[pivot]