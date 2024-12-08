from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        total_sum=sum(nums)
        indx=None
        def split2(l,r):
                ans=total_sum # sum of array is larget ans should be less than
                m=l+(r-l)//2
                while(l<=m and m<=r):
                    lsum=sum(nums[l:m])
                    rsum=sum(nums[m:r])
                    print(m,lsum,rsum,ans)
                    temp_ans=max(lsum,rsum)
                    
                    if temp_ans>=ans:
                         print("break",l,m,r)
                         return indx,ans 
                    if lsum<rsum:
                        # work on rsum and reduce rsum by 
                        ans= min(ans,rsum)
                        indx=m
                        m=m+1
                    else:
                        ans= min(ans,lsum)
                        indx=m
                        m=m-1                
                
        ans=total_sum
        l=0
        r=len(nums)
        for x in range(1,k):
            print(l,r,nums[l:r])
            m,ans1=split2(l,r)
            print("m::",m,ans,nums[l:m],nums[m:r])
            ans=min(ans,ans1)
            if sum(nums[l:m])>sum(nums[m:r]):
                # split left array further
                l,r=l,m
            else:
                # split right array
                l,r=m,r
            
        return ans
                        

if __name__ =="__main__":
    sol=Solution()

    nums = [1,2,3,4,5]
    k = 3
    ans1=9
    nums = [1,4,4]
    k = 2
    ans1=5
    nums = [7,2,5,10,8]
    k = 3
    ans1=18
    nums = [2,3,1,2,4,3]
    k = 5
    ans1=4
    ans=sol.splitArray(nums,k)
    print(nums ,k,"-->ans::",ans,ans1==ans) 

            