# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        total=0
        for i in nums:
            total+=(i-mn)
        return total
