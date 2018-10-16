# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

class Solution(object):
    def dfs(self,i,visited,M,n):
        visited[i] = True
        for x in M[i]:
            if not visited[x]:
                self.dfs(x,visited,M,n)
            
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = [False]*n
        count=0
        M = {key: [] for key in range(n)}
        for x,y in edges:
            M[x].append(y)
            M[y].append(x)
        for i in range(n):
            if not visited[i]:
                count+=1
                self.dfs(i,visited,M,n)
        return count
                
        
