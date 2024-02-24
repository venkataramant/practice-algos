from typing import List

'''
Its 2 pointer problem
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftIndex=0
        rightIndex=len(heights)-1
        maxAns=0
        while(leftIndex<rightIndex):
            ans=min(heights[leftIndex],heights[rightIndex])*(rightIndex-leftIndex)
            maxAns=max(maxAns,ans)
            if heights[leftIndex]<heights[rightIndex]:
                leftIndex+=1
            else:
                rightIndex-=1
        return maxAns

if __name__ =="__main__":
    sol=Solution()
    height = [1,8,6,2,5,4,8,3,7]
    height = [1,1]
    ans=sol.maxArea(height)
    print(height ,"-->ans::",ans)