# https://leetcode.com/problems/subsets-ii/description/

class Solution:
    def dfs(self,nums,index,path,result):
        result.append(path)
        i = index
        while i<len(nums):
            if i>index and nums[i]==nums[i-1]:
                i+=1
                continue
            self.dfs(nums,i+1,path+[nums[i]],result)
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
