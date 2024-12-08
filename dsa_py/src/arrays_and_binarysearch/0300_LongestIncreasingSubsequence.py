from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        incSS=list()
        for num in nums:
            incSS=self.insertIntoList(incSS,num)
            print(incSS,"ans",len(incSS))
        return len(incSS)

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
            print("same as last highest value..ignore it",num,incSS)
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
        print(leftIndex,rightIndex,num,incSS[leftIndex],incSS[rightIndex])
        if incSS[leftIndex]>=num:
            incSS[leftIndex]=num
        elif incSS[rightIndex]>=num:
            incSS[rightIndex]=num

        return incSS
    
    def lengthOfLISWithArray(self, nums: List[int]) -> int:
        nums_len = len(nums)

        lValues = [0]*nums_len
        lValues[0] = 1
        for oIndex in range(1, nums_len):
            tempLV = 0
            for index in range(0, oIndex):
                if nums[index] < nums[oIndex]:
                    tempLV = max(tempLV, lValues[index])
                else:
                    continue
            lValues[oIndex] = tempLV+1
        return max(lValues)


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]  # ans 4
    nums = [0,1,0,3,2,3] # ans 4
    nums = [7,7,7,7,7,7,7] # ans 1
    nums = [4,10,4,3,8,9]
    nums = [4,10,4]
    print(nums, " lengthOfLIS -->", sol.lengthOfLIS(nums))
