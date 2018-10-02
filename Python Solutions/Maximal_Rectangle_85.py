# https://leetcode.com/problems/maximal-rectangle/description/

class Solution:
    def maxAreaHistogram(self,heights):
        if len(heights)==0:
            return 0
        maxArea = 0
        stack = []
        heights.append(0)
    
        for i in range(0,len(heights)):      
            while len(stack)!=0 and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                prevIndex = -1 if len(stack)==0 else stack[-1]
                maxArea = max(maxArea, (i-prevIndex-1)*heights[index])    
            stack.append(i)
            
        heights.pop()
        return maxArea
        
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        x= len(matrix)
        y = len(matrix[0])
        maxArea = 0
        brMatrix = [0 for j in range(y)]
       
        for i in range(x):
            for j in range(y):
                if matrix[i][j]=='1':
                    brMatrix[j]+= 1
                else:
                    brMatrix[j] = 0
            
            maxArea = max(maxArea,self.maxAreaHistogram(brMatrix))
        return maxArea
                        
                    
        
        
