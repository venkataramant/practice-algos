from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct=[]
        rightProduct=[]
        ans=[]
        nums_len=len(nums)
        temp=1
        #rightProduct.append(temp)
        for x in range(nums_len):
           temp=temp*nums[x]
           rightProduct.append(temp)
        temp=1
        for num in nums[::-1]:
            temp=temp*num
            leftProduct.insert(0,temp)
        
        print(leftProduct,rightProduct)
        for x in range(nums_len):
            if x+1>=0 and x+1<nums_len:
                lValue=leftProduct[x+1]
            else:
                lValue=1
            if x-1>=0 and x-1<nums_len:
                rValue=rightProduct[x-1]
            else:
              rValue=1
            ans.append(lValue*rValue)
        return ans
    def best_anser_productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right = [1]
        for num in nums[:-1]:
            left_to_right.append(left_to_right[-1]*num)
            # if len(left_to_right) == 0:
            #     left_to_right.append(num)
            # else:
            #     left_to_right.append(left_to_right[-1]*num)
        
        right_to_left = [1]
        for num in nums[:0:-1]:
            right_to_left.append(right_to_left[-1]*num)
            # if len(right_to_left) == 0:
            #     right_to_left.append(num)
            # else:
            #     right_to_left.append(right_to_left[-1]*num)
        print(left_to_right,right_to_left)
        idx = 0
        for x, y in zip(left_to_right, right_to_left[::-1]):
            temp = x*y
            left_to_right[idx] = temp
            idx = idx + 1
        return left_to_right
    
if __name__ =="__main__":
    sol=Solution()
    nums = [2,3,4,5]
    # nums = [-1,1,0,-3,3]
    # nums = [1,2,3,4]
    ans=sol.best_anser_productExceptSelf(nums)
    print("ans::",ans) 