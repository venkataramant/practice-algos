class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None:
            return False
        rowM = len(matrix)
        rowN = None
        if rowM > 0:
            rowN = len(matrix[0])
        else:
            return False
        left = 0
        right = rowM * rowN
        # print("starting", right, rowM, rowN)
        while(left + 1 < right):
            mid = (left + right) // 2
            
            #midValue = self.getValue(matrix, mid, rowN)
            # print("mid,", mid, midValue)
            midM, midN = mid // rowN, mid % rowN
            midValue = matrix[midM][midN]
            if target == midValue:
                return True
            elif target > midValue:
                left = mid
            else:
                right = mid
        print(left, right)
        if left < (rowM * rowN):
            midM, midN = left // rowN, left % rowN
            midValue = matrix[midM][midN]
            if target == midValue:
                  return True
        if right < (rowM * rowN):
            midM, midN = right // rowN, right % rowN
            midValue = matrix[midM][midN]
            if target == midValue:
                  return True
        return False
    
    def getValue(self, matrix, mid, rowN):
        midM, midN = mid // rowN, mid % rowN
        # print(mid, midM, midN)
        midValue = matrix[midM][midN]
        return midValue
