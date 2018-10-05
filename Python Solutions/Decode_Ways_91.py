# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """  
        if len(s)==1:
            return 0 if s=='0' else 1
        
        dp=[0]*len(s)
        dp[0]= 1 if s[0]!='0' else 0  
        
        if s[1]!='0':
            dp[1]=dp[0]      
        if int(s[:2])<=26 and int(s[:2])>9:
            dp[1]+=1
        for i in range(2,len(s)):
            if s[i]!='0':
                dp[i]=dp[i-1]
            value = s[i-1:i+1]
            if int(value)<=26 and int(value)>9:
                dp[i]+=dp[i-2]
        return dp[len(s)-1]
