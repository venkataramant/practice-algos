from typing import List


class Solution:

    
    def insertIntoList(self,incSS,num):
        nums_len=len(incSS)
        if nums_len==0:
            incSS.append(num)
            return incSS
        if num>incSS[nums_len-1]:
            print("increase the sequence")
            incSS.append(num)
            return incSS
        if num==incSS[nums_len-1]:
            print("same as last highest value..ignore it")
            return incSS
        print(num ," is smaller value...try replace next big value in ",incSS)
            
        leftIndex=0
        rightIndex=nums_len-1
        while(leftIndex<rightIndex-1):
            mid=(leftIndex+rightIndex)//2
            if num==incSS[mid]:
                print("number already there")
                return incSS
            elif num>incSS[mid]:
                leftIndex=mid
            else:
                rightIndex=mid
            print(leftIndex,rightIndex)
        print(leftIndex,rightIndex)
        if incSS[leftIndex]>num:
            incSS[leftIndex]=num
        elif incSS[rightIndex]>num:
            incSS[rightIndex]=num
        return incSS

if __name__ == "__main__":
    sol = Solution()
    incSS=list()
    index=1
    for num in [4,6,10,5,3,9][::]:
        print(num, " insertIntoList -->", sol.insertIntoList(incSS,num))
        if index==4:
            break
        index+=1
        
