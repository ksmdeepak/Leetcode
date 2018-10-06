# https://leetcode.com/problems/dungeon-game/description/

class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        xl = len(dungeon)
        yl = len(dungeon[0])
        dp = [[ 1 for j in range(yl)] for i in range(xl)]
        dp[xl-1][yl-1] = 1 if dungeon[xl-1][yl-1]>0 else abs(dungeon[xl-1][yl-1])+1
        
        for i in range(xl - 2, -1, -1):
            dp[i][yl-1] = max(dp[i + 1][yl - 1] - dungeon[i][yl - 1], 1)
        for j in range(yl - 2, -1, -1):
            dp[xl - 1][j] = max(dp[xl - 1][j + 1] - dungeon[xl - 1][j], 1)
          
        for i in range(xl-2,-1,-1):
            for j in range(yl-2,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]      
        
