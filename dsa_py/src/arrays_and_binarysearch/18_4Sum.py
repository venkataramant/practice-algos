from typing import List

class Solution:
    
    
    def fourSum(self, nums: List[int], target: int) -> List[int]:
        ans_list = set()
        nums_len = len(nums)
        for index in range(nums_len - 2):
            
            leftIndex = index + 1
            while(leftIndex < nums_len-2):
                rightIndex = leftIndex + 1
                second_element_list = set()
                while(rightIndex < nums_len):
                    # print("4th_element_list",second_element_list,rightIndex,nums_len)
                    sValue = target - (nums[rightIndex] + nums[index]+ nums[leftIndex])
                    if sValue not in second_element_list:
                        second_element_list.add(nums[rightIndex])
                    else:
                        ans_list.add(tuple(sorted((nums[index],nums[leftIndex],sValue, nums[rightIndex]))))
                    rightIndex += 1
                leftIndex+=1
           
        return ans_list

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    
    nums = [0, 0, 0]
    nums = [0, 0, 0, 0]
    nums = [0, 1, 1]
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    nums = [-3, -1, 0, 2, 4, 5]
    target = 0
    nums = [2, 2, 2, 2, 2]
    target = 8
    nums = [1,0,-1,0,-2,2]
    target=0

    obj = Solution()
    result = obj.fourSum(nums, target)
    print(result)
