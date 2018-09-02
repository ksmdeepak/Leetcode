class Solution(object):
    def swap(self,nums,x,y):
        nums[x],nums[y] = nums[y],nums[x]
    def sortColors(self, nums):
        
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lo=mid=0
        hi = len(nums)-1
        while mid<=hi:
            if nums[mid]==0:
                self.swap(nums,lo,mid)
                lo+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                self.swap(nums,mid,hi)
                hi-=1
                
       
            
            
                