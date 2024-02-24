from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        ans.append(0)
        for x in range(1,n+1):
            ans.append(x%2 + ans[x//2])
        return ans
    def countBits_best(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
    
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i & 1)
        
        return ans    