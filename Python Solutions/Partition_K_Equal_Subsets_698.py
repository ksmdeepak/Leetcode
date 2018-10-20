# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/

class Solution(object):
    def search(self,target,nums,subsets):
        if len(nums)==0:
            return True
        element = nums.pop()
        for i in range(len(subsets)):
            if subsets[i]+element<=target:
                subsets[i]+=element
                if self.search(target,nums,subsets):
                    return True
                subsets[i]-=element
            if subsets[i]==0:
                break
        nums.append(element)
        return False
                
    
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total%k!=0:
            return False
        else:
            nums=sorted(nums)
            target = total/k
            if nums[-1]>target:
                return False
            while len(nums)>0 and nums[-1]==target:
                nums.pop()
                k-=1
            if k>0:
                return self.search(target,nums,[0]*k)
            else:
                return True
        
