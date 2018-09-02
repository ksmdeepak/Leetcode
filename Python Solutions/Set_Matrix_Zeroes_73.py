class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = False
        column = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0,n):
            if matrix[0][i]==0:
                row=True
        for i in range(0,m):
            if matrix[i][0]==0:
                column=True
        for i in range(1,n):
            if matrix[0][i]!=0:
                for j in range(0,m):
                    if matrix[j][i]==0:
                        matrix[0][i]=0
                        break
        for j in range(1,m):
            if matrix[j][0]!=0:
                for i in range(0,n):
                    if matrix[j][i]==0:
                        matrix[j][0]=0
                        break
        for i in range(1,n):
            if matrix[0][i]==0:
                for j in range(0,m):
                   
                    matrix[j][i]=0
        for j in range(1,m):
            if matrix[j][0]==0:
                for i in range(0,n):
                   
                    matrix[j][i]=0
        if row:
            for i in range(0,n):
                matrix[0][i]=0
        if column:
             for j in range(0,m):
                matrix[j][0]=0
                       
        