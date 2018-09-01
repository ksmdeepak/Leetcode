class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        matrix.reverse()
        n = len(matrix)
        for x in range(0,n):
             for y in range(0,x):
                temp = matrix[x][y]
                matrix[x][y] = matrix[y][x]
                matrix[y][x] = temp
        
        print(matrix)
        