from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

    
        c_total=sum(nums[0:k])
        max_total=c_total
        l_indx=0
        while (l_indx+k<len(nums)):
            #print(max_total,nums[l_indx+k],nums[l_indx])
            c_total=c_total+nums[l_indx+k]-nums[l_indx]
            max_total=max(max_total,c_total)
            #print("c_total after",c_total)
            l_indx+=1
        return max_total/k

if __name__ =="__main__":
    sol=Solution()
    nums = [5]
    k = 1
    ans1=5
    nums = [1,12,-5,-6,50,3]
    k = 4
    ans1=12.75000
    ans=sol.findMaxAverage(nums,k)
    print(nums ,k,"-->ans::",ans,ans1==ans)