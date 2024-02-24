from typing import List
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        lIndx=0
        rIndx=len(s)-1
        #queue=[]
        vowels=('a','e','i','o','u')
        count=0
        ans=0
        for idx in range(len(s)):
            if idx>=k:
                if s[idx-k] in vowels:
                    count-=1
            if s[idx] in vowels:
                count+=1
            ans=max(ans,count)
        return ans
    def maxVowels_notgood(self, s: str, k: int) -> int:

        lIndx=0
        rIndx=len(s)-1
        queue=[]
        vowels=('a','e','i','o','u')
        count=0
        ans=0
        for ch in s:
            if len(queue)==k:
                if queue.pop(0) in vowels:
                    count-=1 
            queue.append(ch)
            if ch in vowels:
                count+=1
            ans=max(ans,count)
        return ans
'''

Output: 3
'''

if __name__ =="__main__":
    sol=Solution()
    s = "abciiidef"
    k = 3
    ans1=3
    s = "aeiou"
    k = 2
    ans1=2
    s = "leetcode"
    k = 3
    ans1=2
    ans=sol.maxVowels(s,k)
    print(s ,k,"-->ans::",ans,ans1==ans)