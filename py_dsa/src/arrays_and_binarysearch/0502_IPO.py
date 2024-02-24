from typing import List
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        capitals=[(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(capitals)
        print(capitals)
        high_profits=[]
        for _ in range (k):
            while capitals and capitals[0][0]<=w:
                c,p=heapq.heappop(capitals)
                heapq.heappush(high_profits,-p)
            if not high_profits:
                break
            w+=-heapq.heappop(high_profits)
            
            
        return w



if __name__ == '__main__':


   
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,1]
    obj = Solution()
    ans=10
    result = obj.findMaximizedCapital(k,w,profits,capital)
    
    print(result,ans,ans==result)