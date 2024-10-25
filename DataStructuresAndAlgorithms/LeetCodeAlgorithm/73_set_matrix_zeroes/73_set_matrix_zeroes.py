
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        
        zeroCoords = []
        
        for row in range(self.rows):
            for col in range(self.cols):
                
                if matrix[row][col] == 0:
                    zeroCoords.append([row,col])
        
        for row, col in zeroCoords:
            self.turnColZero(matrix,col)
            self.turnRowZero(matrix,row)
           
    def turnColZero(self,matrix: List[List[int]], col:int) -> None:
       for row in range(self.rows):
            matrix[row][col] = 0
    
    def turnRowZero(self,matrix: List[List[int]],row:int) -> None:
        
        for col in range(self.cols):
            matrix[row][col] = 0
    def setZeroesSecondMoreEfficient(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0