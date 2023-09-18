

class Solution:

    def __init__(self, maze, target):
        self.maze = maze
        self.target = target
        self.rowMax = len(maze)
        self.colMax = len(maze[0])
        print("init_", self.rowMax, self.colMax, maze[1][3])

    def findElementPosition(self):
        for rowId in range(self.rowMax):
            for colId in range(self.colMax):
                if self.target==self.maze[rowId][colId]:
                    return (rowId,colId)
        return None
                


if __name__ == "__main__":
    
    maze = [[1, 3, 5, 7],
            [8, 9, 10, 12],
            [15, 14, 19, 22],
            [30, 32, 34, 45]
            ]
    target = 0
    sol = Solution(maze, target)
    
    print("findPath -->", sol.findElementPosition(),sol.target)

