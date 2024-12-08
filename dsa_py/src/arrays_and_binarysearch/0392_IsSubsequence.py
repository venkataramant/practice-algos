class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        index1=0
        index2=0
        while(index1<len(s) and index2<len(t)):
            if s[index1]==t[index2]:
                index1+=1
            elif s[index1] not in t[index2:]:
                return False
            index2+=1
        print(index1,len(s))
        if index1==len(s):
            return True
        return False
        