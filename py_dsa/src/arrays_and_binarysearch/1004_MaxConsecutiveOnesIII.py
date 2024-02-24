from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_cns=l=0
        for r, num in enumerate(nums):
            print(l,r,num,max_cns,k)
            k-=1-num
            if k<0:
                # magci
                print("- ",k,nums[l],l)
                k+=1-nums[l]
                l+=1
            else:
                max_cns=max(max_cns,r-l+1)
        return max_cns
    def longestOnes2(self, nums: List[int], k: int) -> int:
        l=0
        ans=0
        for r in range(len(nums)):
            # print(l,r,k,ans)
            if nums[r]==0:
                k-=1  
            if k>=0:
                ans=max(ans,r-l+1)
            else:
                if nums[l]==0:
                    k+=1
                l+=1
                    
        return ans


if __name__ == '__main__':
    nums = [0,1,1,1,0,0,0,1,1,1,1,0]
    k=2
    ans=6
    obj = Solution()
    result = obj.longestOnes(nums,k)
    print(result,ans,ans==result)