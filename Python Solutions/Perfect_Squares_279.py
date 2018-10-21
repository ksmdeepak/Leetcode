# https://leetcode.com/problems/perfect-squares/description/

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        mid = int(math.sqrt(n))+1
        squares = [(i*i) for i in range(int(math.sqrt(n)),0,-1)]
        dp = [n] *(n+1)
        dp[0]=0
        dp[1]=1   
        for i in range(2,n+1):
            for j in squares:
                dp[i]=min(dp[i-j]+1,dp[i])             
        return dp[n]
