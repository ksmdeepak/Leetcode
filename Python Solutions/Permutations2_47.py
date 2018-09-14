class Solution:
    def check(self,nums,start,current):
        i = start
        while i<current:
            if nums[i]==nums[current]:
                return False
            i+=1
        return True
    def getPermutations(self,nums,l,r,output):
        if l==r:
            temp = nums.copy()
            output.append(temp)
        else:
            for i in range(l,r+1):
                if self.check(nums,l,i):
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
        return list(output)
        