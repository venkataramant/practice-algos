'''
Stack
Monotonic Stack -- A monotonic stack is a stack whose elements are monotonically increasing or decreasing

'''
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans=[0]*len(temperatures)
        mystack=[]

        for index,temp in enumerate(temperatures):
            print(index,temp)
            temp_ans=1
            while(len(mystack)>0 and temperatures[mystack[len(mystack)-1]]<temp):
                    temp1=mystack.pop()
                    ans[temp1]=index-temp1
            mystack.append(index)    
            print(mystack,ans)
        return ans

     
    def best_ans_dailyTemperatures(self,temperatures: List[int]) -> List[int]:

        output = [0]*len(temperatures)
        stack = []
        for cindex,ctemp  in enumerate(temperatures):
            while stack and stack[-1][0] < ctemp:#cause it is monotonically decreasing
                    t,i = stack.pop()
                    output[i] = cindex-i
            stack.append((ctemp, cindex))
        return output



if __name__ =="__main__":
    sol=Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    ans=sol.dailyTemperatures(temperatures)
    print("ans::",ans)