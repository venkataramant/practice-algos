from typing import List
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)
        while(l<=r):
            # mid=l+(r-l)//2
            mid =(l+r)//2
            if target==nums[mid]:
                return mid,mid
            elif target>nums[mid]: # target bigger move to left
                l=mid+1
            else:
                r=mid-1
        print(l,r,nums[mid],nums[l],nums[r])
        return l,r


if __name__ == '__main__':


    nums = [-2,-1,0,3,5,9,12,15]
    target = 2
    obj = Solution()
    result = obj.search(nums, target)
    l,r=result
    if l>r:
        l,r=r,l
    print(l,r)
    print(target,result,nums[l:r])
    

