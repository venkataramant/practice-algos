class Solution:

    def longestAlternatingSubarray(self, nums, threshold):
        leftIndex = 0
        nums_len = len(nums)
        last_ans = 0
        even_odd = [0, 1]
        while(leftIndex < nums_len):
            while(leftIndex < nums_len and (nums[leftIndex] % 2 != 0 or nums[leftIndex] > threshold)):
                print("skip", nums[leftIndex])
                leftIndex += 1
                
            new_ans = 0
            if leftIndex >= nums_len:
                print("leftIndex >nums_len")
                break
            print("Checking with array with index", leftIndex)
            index = 0
            while(leftIndex<=nums_len-1 and nums[leftIndex] % 2 == even_odd[index % 2] and nums[leftIndex] <= threshold):
                print("pass", leftIndex, nums[leftIndex], even_odd[index % 2])
                new_ans += 1
                leftIndex += 1
                index += 1
                if leftIndex >= nums_len:
                    print("leftIndex >nums_len..2",leftIndex)
                    break
            if leftIndex<=nums_len-1:
                print("failed at", leftIndex, nums[leftIndex], nums[leftIndex] % 2 , even_odd[index % 2])
            if new_ans > last_ans:
                last_ans = new_ans
        return last_ans

            
if __name__ == "__main__":
    sol = Solution()
    
    nums = [2, 3, 4, 5]
    threshold = 5
    # nums = [8,6,6,4,2,1, 3, -1, -3, 5, 3, 6, 7]
    print(nums, " longestAlternatingSubarray-->", sol.longestAlternatingSubarray(nums, threshold))
