class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
       
        mx = -sys.maxint-1
        mn = sys.maxint
        size = len(prices)
        if size==0:
            return 0
        lmin=[0 for x in range(size)]
        rmax=[0 for x in range(size)]
        for i in range(0,size):
            if prices[i]<=mn:
                mn=prices[i]
            if prices[size-1-i]>=mx:
                mx = prices[size-1-i]
            
            lmin[i] = mn
            rmax[size-1-i] = mx
        mx = -sys.maxint-1
        for i in range(size):
            if rmax[i]-lmin[i]>mx:
                mx = rmax[i]-lmin[i]
        return mx
        