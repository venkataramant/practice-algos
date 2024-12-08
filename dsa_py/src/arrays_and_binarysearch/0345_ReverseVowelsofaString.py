class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=('a', 'e', 'i', 'o','u','A', 'E', 'I', 'O','U')
        lIndex=0
        rIndex=len(s)-1
        s=list(s)
        while(lIndex<rIndex):
            if (s[lIndex]  in vowels and s[rIndex]  in vowels):
                print("found l ",lIndex,s[lIndex])
                print("found r ",rIndex,s[rIndex])
                s[lIndex],s[rIndex]=s[rIndex],s[lIndex]
                lIndex+=1
                rIndex-=1
                continue
            if (s[lIndex] not in vowels):
                lIndex+=1
            if (s[rIndex] not in vowels):
                rIndex-=1
          
        return "".join(s)

    def reverseVowels2(self, s: str) -> str:
        vowels=('a', 'e', 'i', 'o','u','A', 'E', 'I', 'O','U')
        lIndex=0
        rIndex=len(s)-1
        s=list(s)
        while(lIndex<rIndex):
            while(lIndex<len(s) and s[lIndex] not in vowels):
                lIndex+=1
            
            while(rIndex>=0 and s[rIndex] not in vowels):
                rIndex-=1
            if lIndex>rIndex:
                break
            print("found l ",lIndex,s[lIndex])
            print("found r ",rIndex,s[rIndex])
            s[lIndex],s[rIndex]=s[rIndex],s[lIndex]
            lIndex+=1
            rIndex-=1
        return "".join(s)
        