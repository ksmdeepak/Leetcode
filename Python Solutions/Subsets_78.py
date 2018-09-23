#https://leetcode.com/problems/subsets/description/

class Solution(object):
    def generate(self,nums,output,temp,index): 
        if index==len(nums):
            output.append(temp.copy())
            return     
        self.generate(nums,output,temp,index+1)
        self.generate(nums,output,temp+[nums[index]],index+1)
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
       
        self.generate(nums,output,[],0)
        return output
        
        
