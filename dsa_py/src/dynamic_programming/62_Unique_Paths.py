class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans=0
        visited=set()
        results=[[0 for x in range(n)] for y in range(m)]
        for x in range(m-1,-1,-1):
            for y in range(n-1,-1,-1):
                if x==m-1 and y==n-1:
                    results[x][y]=1
                else:
                    if y+1<n:
                        results[x][y]+=results[x][y+1]
                    if x+1<m:
                        results[x][y]+=results[x+1][y]
            results[x]
            
    
        return results[0][0]
