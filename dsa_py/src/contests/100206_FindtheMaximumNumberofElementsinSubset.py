from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(len(nums)):
            mystack=[]
            val=nums[x]
            pIndex=1
            for newIndex in range(x,len(nums)):
                if newIndex
        return nums

if __name__ =="__main__":
    sol=Solution()
    temperatures = [5,4,1,2,2]
    ans=sol.maximumLength(temperatures)
    print("ans::",ans)