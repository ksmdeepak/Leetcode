class Solution(object):
    def binarySearch(self,nums,l,r):
        if(l<=r):
            mid = (int)(r+l/2)
            if mid==0 and nums[mid]>nums[mid+1]:
                return mid
            elif mid==len(nums)-1 and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            else:         
                if (mid+1<len(nums) and nums[mid]>nums[mid+1]) or (mid-1 >=0 and nums[mid]<nums[mid-1]):
                    return self.binarySearch(nums,l,mid-1)
                else:
                    return self.binarySearch(nums,mid+1,r)
        return -1
            
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        else:
            size = len(nums)
            return self.binarySearch(nums,0,size-1)
                