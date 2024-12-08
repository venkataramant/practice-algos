from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_len = len(nums)

        lValues = [0]*nums_len
        lValues[0] = 1
        for oIndex in range(1, nums_len):
            tempLV = 0
            for index in range(0, oIndex):

                if nums[index] < nums[oIndex]:
                    print("less ", nums[index], nums[oIndex], lValues[index])
                    tempLV = min(tempLV, lValues[index])
                else:
                    continue
            lValues[oIndex] = tempLV+1
            print(lValues, oIndex, nums[oIndex])
        return max(lValues)


if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    nums=[1,3,5,4,7]
    # nums = [2,2,2,2,2]
    print(" longestConsecutive-->", sol.longestConsecutive(nums))
