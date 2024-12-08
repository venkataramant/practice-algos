class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None:
            return False
        rowM = len(matrix)
        columnN = None
        if rowM > 0:
            columnN = len(matrix[0])
        else:
            return False
        left = 0
        right = rowM
        # print("determine the row")
        rowId = None
        while(left + 1 < right):
            mid = (left + right) // 2
            
            midValue = matrix[mid][0]
            if target == midValue:
                print("found ..", (mid, 0), matrix[mid][0])
                return True
            elif target > midValue:
                left = mid
            else:
                right = mid
        print(left, right, rowM)
        if left < rowM - 1:
            # midM, midN = left // rowN, left % rowN
            midValue = matrix[left][columnN - 1]
            if target == midValue:
                rowId = left
                print("found ..", (rowId, columnN - 1), matrix[rowId][columnN - 1])
                return True
            elif target < midValue:
                rowId = left
        if right == rowM:
            # midM, midN = right // rowN, right % rowN
            midValue = matrix[right - 1][columnN - 1]
            if target == midValue:
                rowId = right-1
                print("found ..", (right-1, columnN - 1), matrix[right-1][columnN - 1])
                return True
            elif target < midValue:
                rowId = right-1
        
        if rowId == None:
            return False
        nums = matrix[rowId]
        
        left = 0
        right = columnN
        # print("determine the Cell")
        columnId = None
        while(left + 1 < right):
            mid = (left + right) // 2
            
            midValue = nums[mid]
            if target == midValue:
                # print("found ..", (rowId, mid), matrix[rowId][mid])
                return True
            elif target > midValue:
                left = mid
            else:
                right = mid
        print(left, right, rowId)
        if left < columnN - 1:
            # midM, midN = left // rowN, left % rowN
            midValue = nums[left]
            if target == midValue:
                columnId = left
        if right == columnN:
            # midM, midN = right // rowN, right % rowN
            midValue = nums[right - 1]
            if target == midValue:
                columnId = right
        if columnId != None:
            # print("found ..", (rowId, columnId), matrix[rowId][columnId])
            return True
        else:
            return False

        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None:
            return False
        rowM = len(matrix)
        columnN = None
        if rowM > 0:
            columnN = len(matrix[0])
        else:
            return False
        left = 0
        right = rowM * columnN
        # print("starting", right, rowM, columnN)
        while(left + 1 < right):
            mid = (left + right) // 2
            
            #midValue = self.getValue(matrix, mid, columnN)
            # print("mid,", mid, midValue)
            midM, midN = mid // columnN, mid % columnN
            midValue = matrix[midM][midN]
            if target == midValue:
                return True
            elif target > midValue:
                left = mid
            else:
                right = mid
        print(left, right)
        if left < (rowM * columnN):
            midM, midN = left // columnN, left % columnN
            midValue = matrix[midM][midN]
            if target == midValue:
                  return True
        if right < (rowM * columnN):
            midM, midN = right // columnN, right % columnN
            midValue = matrix[midM][midN]
            if target == midValue:
                  return True
        return False
    
    def getValue(self, matrix, mid, columnN):
        midM, midN = mid // columnN, mid % columnN
        # print(mid, midM, midN)
        midValue = matrix[midM][midN]
        return midValue
