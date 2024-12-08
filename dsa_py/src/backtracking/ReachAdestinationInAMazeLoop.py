

class Solution:

    def __init__(self, maze, target):
        self.maze = maze
        self.target = target
        self.rowMax = len(maze)
        self.colMax = len(maze[0])
 
        self.visitedMatrix = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ]
        print(self.visitedMatrix)
        print("init_", self.rowMax, self.colMax, maze[1][3])

    def reachADistination(self):
        rowId, colId = 0, 0
        solutions = list()
        rowId = 0
        colId = 0
        visitedNodes = list()
    
        while(True):
                print("currentNode", rowId, colId)
                if self.maze[rowId][colId] != -1:
                    if [rowId, colId] == self.target:
                        self.visitedMatrix[rowId][colId] = 1
                        visitedNodes.append((rowId, colId))
                        print(self.visitedMatrix, " found the path", visitedNodes)
                        solutions.append(visitedNodes.copy())
                        self.visitedMatrix[rowId][colId] = 0
                        visitedNodes.pop()
                        lastNode = visitedNodes.pop()
                        print("reach target and going to back to ",lastNode)
                        rowId=lastNode[0]
                        colId=lastNode[1]
                    else:
                        # visitedNodes.pop()
                        
                        if self.visitedMatrix[rowId][colId]==0:
                            print("Exploring node first time with right", (rowId, colId))
                            self.visitedMatrix[rowId][colId] = 1
                            visitedNodes.append((rowId, colId))
                            print((rowId, colId), "mark visited and pushed to visitedNodes", visitedNodes)
                            # try going to right
                            if colId < self.colMax-1:
                                colId += 1
                                print("going to Right", (rowId, colId))
                                continue
                            print("Cannot Go Right and try Down")
                        elif self.visitedMatrix[rowId][colId] == 1:
                            print("Exploring node  with down", (rowId, colId))
                            if rowId < self.rowMax-1:
                                rowId += 1
                                print("going to Down", (rowId, colId))
                                continue
                            else:
                                print("Cannot go Down also, back track", visitedNodes)
                                if len(visitedNodes)>0:
                                    lastNode = visitedNodes.pop()
                                    rowId=lastNode[0]
                                    colId=lastNode[1]
                                else:
                                    break
                        else:
                            print("handle here")
                            break
                else:
                    print("this Node is blocked",rowId,colId,visitedNodes)
                    if len(visitedNodes)>0:
                        lastNode = visitedNodes.pop()
                        rowId=lastNode[0]
                        colId=lastNode[1]
                    else:
                        break
                    
        print("came back ", rowId, colId, self.visitedMatrix)
        return solutions
            

if __name__ == "__main__":
    
    maze = [[0, 0, 0, 0],
            [0, 0, -1, 0],
            [-1, 0, -1, 0],
            [0, 0, 0, 0]
            ]
    target = [3, 3]
    sol = Solution(maze, target)
    for sol in sol.reachADistination():
        print(" findPath -->", sol )

