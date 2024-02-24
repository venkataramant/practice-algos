

class Solution:

    def __init__(self, maze, target):
        self.maze = maze
        self.target = target
        self.rowMax = len(maze)
        self.columMax = len(maze[0])
        print("init_", self.rowMax, self.columMax, maze[1][3])

    def reachADistination(self):
        rowId, colId = 0, 0
        solutions = list()
        solution = list()
        isPathExist = self.findPathRec(rowId, colId, solution, solutions)
        return isPathExist, solutions

    def findPathRec(self, rowId, colId, solution, solutions):
        print("findPath ", rowId, colId)
        originStatus = self.checkCurrentOrigin(rowId, colId)
        if originStatus == "REACHED_TARGET":
            rightSol = solution.copy()
            rightSol.append((rowId, colId))
            solutions.append(rightSol)
            return True
        elif originStatus == "EMPTY":
            print("going Left ", [rowId, colId + 1])
            newSolution1 = solution.copy()
            newSolution1.append((rowId, colId))
            isAWayExist = self.findPathRec(rowId, colId + 1, newSolution1, solutions)
            if isAWayExist == False:
                print("newSolution1 is cleard", (rowId, colId + 1), newSolution1)
                newSolution1.clear()
            
            print("going Down ", [rowId + 1, colId])
            newSolution2 = solution.copy()
            newSolution2.append((rowId, colId))
            isAWayExist2 = self.findPathRec(rowId + 1, colId, newSolution2, solutions)
            if isAWayExist2 == False:
                print("newSolution2 is cleard", (rowId + 1, colId), newSolution2)
                newSolution2.clear()
            return isAWayExist or isAWayExist2
            
        else:
            print("OriginStatus ", rowId, colId, originStatus)
            return False 
        return False 

    def checkCurrentOrigin(self, rowId, colId):
        print("checkCurrentOrigin ", [rowId, colId], [self.rowMax, self.columMax])
        if [rowId, colId] == self.target:
            return "REACHED_TARGET"
        elif rowId >= self.rowMax or colId >= self.columMax:
            return "OUT_OF_MAZE"
        else:
            if self.maze[rowId][colId] == -1:
                return "BLOCKED"
            else:
                return "EMPTY"



if __name__ == "__main__":
    
    maze = [[0, 0, 0, 0],
            [0, 0, -1, 0],
            [0, -1, -1, 0],
            [0, 0, 0, 0]
            ]
    target = [3, 3]
    sol = Solution(maze, target)
    
    print(" findPath -->", sol.reachADistination())

