from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def dfs(i,level,cur):
            print("calling level",level, i,cur)
            if i==len(nums):
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i+1,level+1,cur)
            cur.pop()
            while(i+1<len(nums) and nums[i]==nums[i+1]):
                i+=1
            dfs(i+1,level+1,cur)
        dfs(0,0,[])
        return ans
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        cur=[]
        nums.sort()
        def dfs(i):
            if i>=len(nums):
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            while(i+1<len(nums) and nums[i]==nums[i+1]):
                i+=1
            dfs(i+1)
        dfs(0)
        return ans
    
    def subsetsWithDup_recur(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        nums.sort()
        len_nums=len(nums)
        ans.append([nums[0]])
        prev=nums[0]
        i=1
        last_batch_size=1
        for i in range(1,len_nums):
            print(ans,i,nums[i],prev,last_batch_size)
            start_index=0
            len2=len(ans)
            print("len2",len2)
            if nums[i]==prev:
                start_index=last_batch_size
                last_batch_size+=len2-start_index
            for x in range(start_index,len2):
                temp=ans[x].copy()
                temp.append(nums[i])
                ans.append(temp)
            prev=nums[i]
            last_batch_size=len2
  
        return ans

if __name__=="__main__":
    nums = [1,2,3]
    ans= [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    nums = [4,4,4,1,4]
    ans = [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
    sol=Solution()
    ans2=sol.subsetsWithDup(nums)
    print(nums," subsetsWithDup ",sorted(ans2)==sorted(ans))
    print(sorted(ans2))
    print(sorted(ans))                