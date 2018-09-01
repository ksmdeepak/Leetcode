class Solution:
    def getPermutations(self,nums,l,r,output):
        if l==r:
            temp = nums.copy()
            if temp not in output:
                output.append(temp)
        else:
            for i in range(l,r+1):
                nums[l],nums[i] = nums[i],nums[l]
                self.getPermutations(nums,l+1,r,output)
                nums[l],nums[i] = nums[i],nums[l]
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
        self.getPermutations(nums,0,len(nums)-1,output)
        return output
        