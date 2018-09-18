# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def binarySearchRow(self,arr,l,r,target):    
        if l<=r:
            mid = (int)((r+l)/2)
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                return self.binarySearchRow(arr,l,mid-1,target)
            else:
                return self.binarySearchRow(arr,mid+1,r,target)
        return -1
    def binarySearchCol(self,matrix,l,r,target):
        print("rc")
        if l<=r:
            mid = (int)((r+l)/2)
            if matrix[mid][0]==target:
                return mid
            elif matrix[mid][0]<target and mid+1<len(matrix) and matrix[mid+1][0]>target:
                return mid
            elif matrix[mid][0]>target and mid-1>=0 and matrix[mid-1][0]<target:
                return mid-1
            elif matrix[mid][0]>target:
                return self.binarySearchCol(matrix,l,mid-1,target)
            else:
                return self.binarySearchCol(matrix,mid+1,r,target)
        return -1
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """ 
        if len(matrix)==0:
            return False
        elif len(matrix[0])==0:
            return False
        else:
            row = self.binarySearchCol(matrix,0,len(matrix)-1,target)
            if matrix[row][0]==target:
                return True
            else:
                found = self.binarySearchRow(matrix[row],0,len(matrix[row])-1,target)
                if found==-1:
                    return False
                else:
                    return True
        
