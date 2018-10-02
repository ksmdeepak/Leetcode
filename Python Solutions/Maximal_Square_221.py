#

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        x = len(matrix)
        y = len(matrix[0])
        maxK = 0
        brMatrix = [[0 for j in range(y)] for i in range(x)]    
        for i in range(x):
            for j in range(y):
                if i==0 or j==0:
                    brMatrix[i][j] = int(matrix[i][j])
                    maxK = max(maxK,brMatrix[i][j])
                else:
                    if matrix[i][j]=='1':
                        brMatrix[i][j] = min(brMatrix[i-1][j],brMatrix[i][j-1],brMatrix[i-1][j-1])+1
                        maxK = max(maxK,brMatrix[i][j])
       
        return maxK**2
                        
                    
