from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() # sort them
        lIndx=0
        rIndx=len(nums)-1
        ans=0
        # print(nums)
        while(lIndx<rIndx):
            # print(nums[lIndx],nums[rIndx])
            if k==nums[lIndx]+nums[rIndx]:
                ans+=1
                rIndx-=1
                lIndx+=1
            elif k<nums[lIndx]+nums[rIndx]: # Greater reduce bigger one
                rIndx-=1
            else: # Smaller increase smaller one
                lIndx+=1
        return ans

if __name__ =="__main__":
    sol=Solution()
    nums = [1,2,3,4]
    k = 5
    ans1=2
    nums = [3,1,3,4,3]
    k = 6
    ans1=1
    ans=sol.maxOperations(nums,k)
    print(nums ,k,"-->ans::",ans,ans1==ans) 