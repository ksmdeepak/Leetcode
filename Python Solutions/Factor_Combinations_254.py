# https://leetcode.com/problems/factor-combinations/description/

class Solution:
    def __init__(self):
        self.output=set()
    def dfs(self,n,path):
        if n==1:
            return
        if len(path)>0:
            temp = sorted(path.copy()+[n])
            self.output.add(tuple(temp))
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:    
                self.dfs(n//i,path+[i])   
        
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.dfs(n,[])
        return list(self.output)
        
