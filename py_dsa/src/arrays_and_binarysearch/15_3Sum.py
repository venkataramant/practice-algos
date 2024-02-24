from typing import List


class Solution:
    
    def threeSum(self, nums: List[int]) -> List[int]:
        ans_list = set()
        nums_len = len(nums)
        for index in range(nums_len - 1):
            leftIndex = index + 1
            second_element_list = set()
            while(leftIndex < nums_len):
                print("second_element_list",second_element_list,leftIndex,nums_len)
                sValue = 0 - (nums[leftIndex] + nums[index])
                if sValue not in second_element_list:
                    second_element_list.add(nums[leftIndex])
                else:
                    self.addToAns(ans_list,nums[index], sValue, nums[leftIndex])
                    #ans = [nums[index], sValue, nums[leftIndex]]
                    #ans.sort()
                    #ans_list.add(tuple(ans))
                    
                    # ans_list.add(tuple(sorted((nums[index],sValue, nums[leftIndex]))))
                leftIndex += 1
           
        return ans_list
        
    def addToAns(self, ans_list, val1, val2, val3):
        if val1 >= val2 and val1 >= val3:
            if val2 >= val3:
                ans_list.add((val1, val2, val3))
            else:
                ans_list.add((val1, val3, val2))
                             
        elif val2 >= val1 and val2 >= val3:
            if val1 >= val3:
                ans_list.add((val2, val1, val3))
            else:
                ans_list.add((val2, val3, val1))
        elif val3 >= val1 and val3 >= val2:
            if val1 >= val2:
                ans_list.add((val3, val1, val2))
            else:
                ans_list.add((val3, val2, val1))


if __name__ == '__main__':
    nums = [-4, -1, -1, -1, 0, 1, 2]
    
    
    nums = [0, 0, 0, 0]
    nums = [0, 1, 1]
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [0, 0, 0]
    obj = Solution()
    result = obj.threeSum(nums)
    print(result)
