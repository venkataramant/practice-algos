'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''


class Solution:

    def maxSlidingWindow(self, nums, k):

        return self.findoutSolution(nums, k, 0, list())

    def findoutSolution_memory_out(self, nums, k, index=0, ans=list()):
        if len(nums) > k:
            ans.insert(index, max(nums[0:k]))
            ans.insert(index + 1, max(nums[len(nums) - k:]))
        elif len(nums) == k:
            ans.insert(index, max(nums[0:k]))
        else:
            return ans
        print(nums, index, ans, nums[0:k], nums[len(nums) - k:])
        return self.findoutSolution(nums[1:len(nums) - 1], k, index + 1, ans)

    def findoutSolution2(self, nums, k, index, ans):
        print(nums, index, ans, nums[0:k], nums[len(nums) - k:])
        if len(nums) < k:
            return ans
        elif len(nums) > k:
            ans.insert(index, max(nums[0:k]))
            ans.insert(index + 1, max(nums[len(nums) - k:]))
            return self.findoutSolution(nums[1:len(nums) - 1], k, index + 1, ans)
        else:
            ans.insert(index, max(nums[0:k]))
            return ans

    def findoutSolution(self, nums, k, index, ans):
        if len(nums) < k:
            return ans
        elif len(nums) > k:
            solution1 = max(nums[0:k])
            solution2 = max(nums[len(nums) - k:])
            self.findoutSolution(nums[1:len(nums) - 1], k, index + 1, ans)
            print(nums,index,solution1,solution2,ans)
            ans.insert(0, solution1)
            ans.insert(len(nums), solution2)
            return ans
        else:
            ans.insert(index, max(nums[0:k]))
            return ans


if __name__ == "__main__":
    sol = Solution()
    
    nums = [5, 3, 4]
    nums = [7, 2, 4]
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("sol-->", sol.maxSlidingWindow(nums, k), sol.maxSlidingWindow(nums, k) == [3, 3, 5, 5, 6, 7])
