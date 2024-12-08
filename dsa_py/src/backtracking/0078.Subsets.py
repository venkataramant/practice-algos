from typing import List
class Solution:
    def subsets_loop(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for num in nums:
            ans_len=len(ans)
            for x in range(ans_len):
                temp=ans[x].copy()
                temp.append(num)
                ans.append(temp)
        return ans
    def subsets_recursive(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        def backtracking(i):
            if i>=len(nums):
                return
            ans_len=len(ans)
            for x in range(ans_len):
                temp=ans[x].copy()
                temp.append(nums[i])
                ans.append(temp)
            backtracking(i+1)
        
        backtracking(0)
        return sorted(ans)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        subset=[]
        def dfs(i):
            
            if i>=len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return ans
            

if __name__=="__main__":
    nums = [1,2,3]
    ans= [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    sol=Solution()
    ans2=sol.subsets(nums)
    print(nums," Subsets ",ans2,sorted(ans2)==sorted(ans),ans)