from typing import List


class Solution:
    
    def twoSum2PointersForSortedNums(self, nums, target, preFixValue):
        ans_list = list()
        
        leftIndex = 0
        nums_len = len(nums)
        rightIndex = nums_len - 1
        while(leftIndex < rightIndex and rightIndex > 0):
            sValue = nums[leftIndex] + nums[rightIndex]
            if sValue == target:
                ans_list.append([preFixValue,nums[leftIndex], nums[rightIndex]])
                # leftIndex += 1
                # rightIndex -= 1
                tLeft = leftIndex
                while(leftIndex < nums_len - 1 and nums[tLeft] == nums[leftIndex]):
                    print("left")
                    leftIndex += 1
                tRight = rightIndex
                while(rightIndex > 0 and nums[tRight] == nums[rightIndex - 1]):
                    print("right")
                    rightIndex -= 1
                
            elif sValue > target:
                rightIndex -= 1
            else:
                leftIndex += 1
           
        return ans_list
        
    def threeSum(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        ans_list = list()
        nums_len = len(nums)
        index = 0
        while (index < nums_len - 1):
            target = 0 - nums[index]
            temp_ans_list = self.twoSum2PointersForSortedNums(nums[index + 1:], target,nums[index])
            
            if len(temp_ans_list) != 0:
                print(index, nums[index], temp_ans_list) 
                # [ans.insert(0, nums[index]) for ans in temp_ans_list]
                ans_list = ans_list + temp_ans_list
            tIndex = index
            while(index < nums_len - 1 and nums[tIndex] == nums[index]):
                index += 1
            # index += 1
        return ans_list


if __name__ == '__main__':
    nums = [-4, -1, -1, -1, 0, 1, 2]
    
    nums = [0, 0, 0]
    nums = [0, 0, 0, 0]
    nums = [0, 1, 1]
    nums = [-1, 0, 1, 2, -1, -4]
    obj = Solution()
    result = obj.threeSum(nums)
    print(result)
