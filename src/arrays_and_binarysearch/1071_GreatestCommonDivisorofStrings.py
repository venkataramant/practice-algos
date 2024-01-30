class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)<len(str2):
            return self.gcdOfStrings(str2,str1)
        len1=len(str1)
        len2=len(str2)
        ans=""
        for x in range(len2,0,-1):
            tempAns=str2[-x:]
            print(tempAns,x)
            index=len(tempAns)
            if index!=0 and len2 % (index)==0 and len1 % (index)==0:
                
                if str2==tempAns* (len2 //index) and str1==tempAns* (len1 //index):
                    ans= tempAns
                    break
        return ans
    def gcdOfStrings_working(self, str1: str, str2: str) -> str:
        if len(str1)<len(str2):
            return self.gcdOfStrings(str2,str1)
        len1=len(str1)
        len2=len(str2)
        ans=""
        for x in range(0,len2):
            index=len2-x
            if len2 % (index)==0 and len1 % (index)==0:
                tempAns=str2[0:index]
                if str2==tempAns* (len2 //index) and str1==tempAns* (len1 //index):
                    ans= tempAns
                    break
        return ans
    def gcdOfStrings_max(self, str1: str, str2: str) -> str:
        if len(str1)<len(str2):
            return self.gcdOfStrings(str2,str1)
        len1=len(str1)
        len2=len(str2)
        ans=""
        for x in range(len2,0,-1):
            if len1 % x==0:
                tempAns=str2[0:x]
                if str1==tempAns* (len1 // x):
                    ans= tempAns
                
        return ans

class BestSolution:
    from math import gcd
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]

if __name__ =="__main__":
    sol=Solution()
    str1 = "ABABAB"
    str2 = "ABABAB"
    # str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    # str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
   
    ans=sol.gcdOfStrings(str1,str2)
    print("ans::",ans)