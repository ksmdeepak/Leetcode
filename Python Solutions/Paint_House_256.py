# https://leetcode.com/problems/paint-house/description/

class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        x = len(costs)
        if x==0:
            return 0
        
        pR = costs[0][0]
        pB = costs[0][1]
        pG = costs[0][2]
        
        for i in range(1,x):
            curR = min(pB,pG) + costs[i][0]
            curB = min(pR,pG) + costs[i][1]
            curG = min(pR,pB) + costs[i][2]
            pR,pB,pG = curR,curB,curG
       
        return min(pR,pB,pG)
