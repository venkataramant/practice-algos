from typing import List
class Solution:
     def countKeyChanges(self, s: str) -> int:
        count=0
        for x in range(len(s)):
            if x>=len(s)-1:
                return count
            if s[x+1].lower()!=s[x].lower():
                count+=1
        return count



if __name__ =="__main__":
    sol=Solution()
    s = "aAbBcC"
    ans=sol.countKeyChanges(s)
    print("ans::",ans)