# https://leetcode.com/problems/distinct-subsequences/description/

class Solution:    
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(t)
        n = len(s)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m+1):
            for j in range(1,n+1):  
                if t[i-1]==s[j-1]:    
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[m][n]
