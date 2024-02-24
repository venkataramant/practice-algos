class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # after best inputs
        index=0
        new_s=""
        for index in range(0,len(s),2*k):
            rightIndex=min(index+k-1,len(s))
            new_s+=s[index:rightIndex+1][::-1]
            new_s+=s[rightIndex+1:index+(2*k)]
        
        return new_s

    def reverseStrMB(self, s: str, k: int) -> str:
        index=0
        new_s=list()
        while((index+k)<len(s)):
            leftIndex=index
            rightIndex=index+k-1
            print("reversing",s[leftIndex:rightIndex+1])
            new_s.append(s[leftIndex:rightIndex+1][::-1])
            new_s.append(s[leftIndex+k:leftIndex+(2*k)])
            index+=2*k
        leftIndex=index
        rightIndex=max(index+k-1,len(s))
        # new_s.append(s[rightIndex])
        new_s.append(s[leftIndex:rightIndex+1][::-1])
           
        print(new_s,index)
        return "".join(new_s)
    
    def reverseStrBFRC(self, s: str, k: int) -> str:
        index=0
        new_s=list()
        while((index+k)<len(s)):
            leftIndex=index
            rightIndex=index+k-1
            while(leftIndex<=rightIndex):
                new_s.append(s[rightIndex])
                rightIndex-=1
            new_s.append(s[leftIndex+k:leftIndex+(2*k)])
            index+=2*k
        leftIndex=index
        rightIndex=index+k-1
        while(leftIndex<=rightIndex):
            if rightIndex<len(s):
                new_s.append(s[rightIndex])
            rightIndex-=1
            new_s.append(s[leftIndex+k:leftIndex+(2*k)])
            index+=2*k
        print(new_s,index)
        return "".join(new_s)

if __name__ == "__main__":
    sol = Solution()
    s = "abcdefg"
    k = 2 # Output: "bacdfeg"
    s = "abcd"
    k = 2 #Output: "bacd"
    print(nums, " lengthOfLIS -->", sol.lengthOfLIS(nums))