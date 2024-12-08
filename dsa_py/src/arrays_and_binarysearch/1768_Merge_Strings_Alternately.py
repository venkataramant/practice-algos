class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        len1=len(word1)
        len2=len(word2)
        minLen=len1
        if len1>len2:
            minLen=len2
        x=0
        while x< minLen:
            ans.append(word1[x])
            ans.append(word2[x])
            x+=1
        if len1>len2:
            ans.append(word1[len2:])
        else:
            ans.append(word2[len1:])
        return "".join(ans)

if __name__ =="__main__":
    sol=Solution()
    word1="135ace"
    word2="246bdfg"
    ans=sol.mergeAlternately(word1,word2)
    print("ans::",ans)