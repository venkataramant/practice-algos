class Solution:

    def sumOfSquares(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return 0
 
        ss = 0
        nums_len = len(nums)
        dividors = set()
        ss = ss + (nums[0] * nums[0])
        index = 2
        while(index <= nums_len // 2):
            print("index", index, dividors)
            if  index not in dividors:
                if nums_len % index == 0:
                    seq = 1
                    while(index * seq <= nums_len // 2):
                        ss = ss + (nums[index * seq - 1] * nums[index * seq - 1])
                        dividors.add(index * seq)
                        seq += 1
            index += 1
                    
        if nums_len > 1:
            ss = ss + (nums[nums_len - 1] * nums[nums_len - 1])
        return ss

    def sumOfSqares2(self, nums):
        index = 1
        sumOfSquares = 0
        nums_len = len(nums)
        while(index <= nums_len // 2):
            print("index", index)
            if nums_len % index == 0:
                print("found", nums[index - 1])
                sumOfSquares = sumOfSquares + (nums[index - 1] * nums[index - 1])
            index += 1
        if nums_len > 1:
            sumOfSquares = sumOfSquares + (nums[nums_len - 1] * nums[nums_len - 1])
        return sumOfSquares


if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    nums = [1, 2, 3, 4]
    nums = [2, 7, 1, 19, 18, 3]
    nums = [9, 32, 13, 30, 10, 40, 28, 40]
    nums = [42, 34, 45, 6, 20, 28, 24, 40, 41, 7]
    # nums = [100, 200, 4] 
    print(nums, " sumOfSquares -->", sol.sumOfSquares(nums))
