class Solution:

    def searchMatrix(self, matrix, target) -> bool:
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
            
            midValue = self.getValue(matrix, mid, columnN)
            # print("mid,", mid, midValue)
            if target == midValue:
                return True
            elif target > midValue:
                left = mid
            else:
                right = mid
        print(left, right)
        if left < (rowM * columnN):
              if target == self.getValue(matrix, left, columnN):
                  return True
        if right < (rowM * columnN):
              if target == self.getValue(matrix, right, columnN):
                  return True
        return False
    
    def getValue(self, matrix, mid, columnN):
        midM, midN = mid // columnN, mid % columnN
        # print(mid, midM, midN)
        midValue = matrix[midM][midN]
        return midValue


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 20
    print(" searchMatrix -->", sol.searchMatrix(matrix, target))

