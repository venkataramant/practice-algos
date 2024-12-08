class Solution:
    def reverseWords(self, str1: str) -> str:
        ans=list()
        str1=word1.strip()
        isStartNewWord=False
        word_len=len(str1)
        ans.append(str1[0])

        for index in range(1,word_len):
            newCh=str1[index]
            if newCh==" ":
                isStartNewWord=True
                wordIndex=0
                continue
            else:
                if isStartNewWord:
                    ans.insert(wordIndex," ")
                    ans.insert(wordIndex,newCh)
                    isStartNewWord=False
                else:
                    ans.insert(wordIndex,newCh)
                wordIndex+=1
            print(newCh,ans)

        return "".join(ans)

# Other Approaches
'''
        1 
        ' '.join(s.split()[::-1])
        2
        result = s.split()
        result.reverse()
        return " ".join(result)

'''
if __name__ =="__main__":
    sol=Solution()
    word1= "a good   example"
    
    word2="example good a"
    ans=sol.reverseWords(word1)
    print("ans::",ans)