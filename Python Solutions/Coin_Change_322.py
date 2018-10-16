# https://leetcode.com/problems/coin-change/description/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """  
        coins = set(coins)
        dp = [sys.maxsize]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            if i in coins:
                dp[i] = 1
            else:
                for j in coins:
                    if j<i:
                        dp[i] = min(dp[i],dp[i-j]+1)
        return dp[amount] if dp[amount]<sys.maxsize else -1
        
        
