class Solution(object):
    def findPivot(self,nums,l,r):
        mid = l + int((r-l)/2)   
        if(l<=r):
            if mid==0 and nums[mid]>nums[mid+1]:
                return mid
            elif mid==len(nums)-1 and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            else:           
                if nums[0]<=nums[mid]:
                    return self.findPivot(nums,mid+1,r)
                else:
                    return self.findPivot(nums,l,mid-1)
        return -1
    
    def binarySearch(self,nums,target,l,r):
        mid = l + int((r-l)/2)
        if(l<=r):
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]<target:
                    return self.binarySearch(nums,target,mid+1,r)
                else:
                    return self.binarySearch(nums,target,l,mid-1)
        return -1
        
    def search(self, nums, target):
       
        if(len(nums)==0):
            return -1
        elif len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        pivot=self.findPivot(nums,0,len(nums)-1)
        print(pivot)
        if(target<nums[0]):
            return self.binarySearch(nums,target,pivot+1,len(nums)-1)
        else:
            return self.binarySearch(nums,target,0,pivot)