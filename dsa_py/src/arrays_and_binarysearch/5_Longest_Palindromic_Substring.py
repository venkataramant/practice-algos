class Solution:
    # Dynmaic programming
    # Build from known subset and make it bigger/smaller
    def longestPalindrome(self, s: str) -> str:
        def find_longest_pdm(left_index,right_index,s):
            print(left_index,right_index)
            c_pdm=""
            while(left_index>=0 and right_index<=len(s)-1):
                #print(s[left_index],s[right_index])
                if s[left_index]!=s[right_index]:
                    return c_pdm
                else:
                    c_pdm=s[left_index:right_index+1]
                    left_index=left_index-1
                    right_index=right_index+1
            return c_pdm

        longest_pdm=""
        for index in range(len(s)):
            temp_pdm=find_longest_pdm(index,index,s)
            # print(longest_pdm,temp_pdm)
            if len(longest_pdm)<len(temp_pdm):
                longest_pdm=temp_pdm
            temp_pdm=find_longest_pdm(index,index+1,s)
            # print(longest_pdm,temp_pdm)
            if len(longest_pdm)<len(temp_pdm):
                longest_pdm=temp_pdm
    
        return longest_pdm
        
       

if __name__ =="__main__":
    sol=Solution()
    s = "babad"
    ans1="bab"
    # s = "cbbd"
    # ans1="bb"
    ans=sol.longestPalindrome(s)
    print("ans1::",ans1,ans,ans==ans1)
