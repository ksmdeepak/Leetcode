class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        start =0 
        count =0 
        while count < len(nums):
            current = start     
            prev = nums[start]
            flag =0 
            while start!=current or flag==0:
                flag+=1
                nex = (current+k)%len(nums)
                temp = nums[nex]
                nums[nex] = prev
                prev = temp
                current = nex
                count+=1
                
            start+=1
            