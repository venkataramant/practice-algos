from typing import List
import heapq
class Solution:
    def rob(self, nums: List[int]) -> int:
        last_amount=0
        last_2_amount=0
        for num in nums:
            print(num,last_amount,last_2_amount)
            last_amount,last_2_amount=max(last_2_amount+num,last_amount),last_amount

        return last_amount if last_amount>last_2_amount else last_2_amount
    
    def rob_over_memory(self, nums: List[int]) -> int:
        robbed_amount=dict()
        for x in range(len(nums)):
            included=nums[x]+ robbed_amount.get(x-2,0)
            not_included=robbed_amount.get(x-1,0)
            if included>not_included:
                robbed_amount[x]=included
            else:
                robbed_amount[x]=not_included
        print(robbed_amount)
        return robbed_amount[len(nums)-1]
    def rob_not_optim(self, nums: List[int]) -> int:
        robbed=set()
        max_ans=0
        def dfs(i,cur_val):
            nonlocal max_ans
            if i>=len(nums):
                max_ans=max(max_ans,cur_val)
                return
            dfs(i+2,cur_val+nums[i])

            dfs(i+1,cur_val)
        dfs(0,0)
        return max_ans
    
    def rob_wrong(self, nums: List[int]) -> int:
        robbed=set()
        ans=0
        houses=[(-x,y) for x, y in zip(nums,range(len(nums)))]
        print(houses)
        heapq.heapify(houses)
        print(houses[0])
        while(houses):
            house=heapq.heappop(houses)
            if house[1]+1 not in robbed and house[1]-1 not in robbed:
                robbed.add(house[1])
                ans+=-house[0]

        return ans


if __name__=="__main__":
    nums = [1,2,3,1]
    ans= 4
    nums=[2,1,1,2]
    ans=4
   
    sol=Solution()
    ans2=sol.rob(nums)
    print(nums," rob ",ans2==ans,ans2,ans)               
        
        