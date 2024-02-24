from typing import List
from ast import Num


class Solution:
    
    def twoSumSorted2Pointers(self, nums, target):
        ans_list = list()
        nums.sort()
        leftIndex = 0
        rightIndex = len(nums) - 1
        while(leftIndex < rightIndex):
            sValue = nums[leftIndex] + nums[rightIndex]
            if sValue == target:
                ans_list.append((nums[leftIndex], nums[rightIndex]))
                rightIndex -= 1
            elif sValue > target:
                rightIndex -= 1
            else:
                leftIndex += 1
                
        return ans_list
    
    def twoSumNonSortedSearchRight(self, nums, target):
        ans_list = list()
        for index in range(len(nums)):
            if target - nums[index] in nums[index + 1:]:
                ans_list.append((nums[index], target - nums[index]))
        return ans_list
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSumSorted2Pointers(nums, target)


if __name__ == '__main__':
    target = 7

    nums = [4, 4, 5, 7, 3, 8, 0, 2]
    
    nums = [-1, 0, 2, 4]
    target = 2

    obj = Solution()
    result = obj.twoSum(nums, target)
    print(result)
