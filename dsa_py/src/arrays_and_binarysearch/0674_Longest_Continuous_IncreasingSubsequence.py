from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        nums_len = len(nums)
        startIndex = 0
        lss = 1
        templss = 1
        while (startIndex+1 < nums_len):
            if nums[startIndex] < nums[startIndex+1]:
                templss += 1
            else:
                lss = max(templss, lss)
                templss = 1
            startIndex += 1
        return max(templss, lss)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 5, 4, 7]
    print(" findLengthOfLCIS-->", sol.findLengthOfLCIS(nums))
