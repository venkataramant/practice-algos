from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r,ans=0,0,0
        zero_exists=False
        z_index=None
        while(r<len(nums)):
            print(nums[r],l,r,zero_exists,ans,z_index)
            if nums[r]==0 and zero_exists==True:
                l=z_index+1
            ans=max(ans,r-l+1)
            if nums[r]==0:
                zero_exists=True
                z_index=r
            r+=1
        return ans-1



if __name__ =="__main__":
    sol=Solution()
    nums = [0,1,1,1,0,1,1,0,1]
    correct_ans=5
    nums = [1,1,0,1]
    correct_ans=3
    nums = [1,1,1]
    correct_ans=2
    
    ans=sol.longestSubarray(nums)
    print(nums ,"-->longestSubarray::",ans,correct_ans,ans==correct_ans)