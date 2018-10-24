# https://leetcode.com/problems/subarray-sum-equals-k/description/

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = {}
        count[0] = 1
        total = 0
        output = 0
        for i in range(n):
            total+=nums[i]
            if total-k in count:
                output+=count[total-k]
            if total in count:
                count[total]+=1
            else:
                count[total]=1
        return output
            

        
