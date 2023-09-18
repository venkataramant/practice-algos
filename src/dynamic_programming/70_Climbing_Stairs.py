class Solution:

    def climbStairs(self, n):
        countMap = {}
        return self.findWays(n, countMap)

    def findWays(self, n, countMap):
        print(countMap)
        if n <= 0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        if n in countMap:
            print(countMap)
            print("cache,", n, countMap[n])
            return countMap[n]
        for x in range(0, n + 1):
            countMap[x] = self.findWays(x - 1, countMap) + self.findWays(x - 2, countMap)
        return countMap[n]
    
    def climbStairs2(self, n: int) -> int:
        countMap = {}
        for x in range(n + 1):
            select = list()
            solutions = list()
            solutionCount = self.findAnswerWithCase(x, select, solutions, countMap)
            countMap[x] = solutionCount
        return countMap[n]
    
    def findAnswerWithCase(self, n, select=list(), solutions=list(), countMap=dict()):
        if n - 1 in countMap and n - 2 in countMap:
            return countMap[n - 1] + countMap[n - 2]
        if sum(select) == n:
            solutions.append(1)
            return len(solutions)
        if sum(select) > n:
            return len(solutions)
        c_select_1 = select.copy()
        c_select_2 = select.copy()
        c_select_1.append(1)
        c_select_2.append(2)
        sol1 = self.findAnswerWithCase(n, c_select_1, solutions, countMap)
        sol2 = self.findAnswerWithCase(n, c_select_2, solutions, countMap)
        if sol1 > sol2:
            return sol1
        else:
            return sol2

    def findAnswer3(self, n, lastSteps=0, solutions=dict()):
    
        if lastSteps == n:
            return 1
        if lastSteps > n:
            return 0
        count1 = self.findAnswer3(n, lastSteps + 1)
        count2 = self.findAnswer3(n, lastSteps + 2)
        return count1 + count2
        

if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(n, " no of climbStairs -->", sol.climbStairs(n))
