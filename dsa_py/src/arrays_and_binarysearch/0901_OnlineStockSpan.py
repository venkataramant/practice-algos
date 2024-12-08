
'''
Stack
Monotonic Stack -- A monotonic stack is a stack whose elements are monotonically increasing or decreasing

'''
class StockSpanner:

    def __init__(self):
        pass

    def next(self, price: int) -> int:
        pass


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
    
from typing import List
class Solution:
    def __init__(self):
        
        self.prices=[]
        self.stack=[]
    def get_top_of_stack(self):
        return self.stack and self.stack[-1]
    def pop_stack(self):
        return self.stack and self.stack.pop()
    def push_stack(self, val):
        self.stack.append(val)

    def next(self, price: int) -> int:
        self.prices.append(price)
        ans=1
        while True:
            top=self.get_top_of_stack()
            if top and top[0]<=price:
                 ans=ans+top[1]
                 self.pop_stack()
            else:
                break
        self.push_stack((price,ans))
        return ans
    def find_ans(self,prices):
        ans=[]
        for price in prices:
            ans.append(self.next(price))
        return ans

if __name__ =="__main__":
    sol=Solution()
    nums = [1,2,3,4]
    prices=[28,14,28,35,46,53,66,80,87,88] # ans 1,1,3,4,5,6,7,8,9,10
    prices= [100,80,60,70,60,75,85] # ans 1,1,1,2,1,4,6
    
    ans=sol.find_ans(prices)
    print("ans::",ans)