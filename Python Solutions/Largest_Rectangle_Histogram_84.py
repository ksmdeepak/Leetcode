#https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
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
        return maxArea
                
