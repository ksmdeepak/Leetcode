# https://leetcode.com/problems/subsets-ii/description/

class Solution:
    def dfs(self,nums,index,path,result):
        result.append(path)
        i = index
        while i<len(nums):
            self.dfs(nums,i+1,path+[nums[i]],result)
            i+=1
            while i<len(nums) and nums[i]==nums[i-1]:
                i+=1
            
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path=[]
        result=[]
        nums.sort()
        self.dfs(nums,0,path,result)
        return result
