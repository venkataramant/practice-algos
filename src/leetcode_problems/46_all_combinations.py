class Solution:

    def permute(self, nums):
        solutions = list()
        selection = list()
        self.fetchAll(nums, len(nums), selection, solutions)
        return  solutions

    def fetchAll(self, nums, selectSize, selection=None, solutions=list()):
        solutions.append(selection.copy())
        if len(selection) == selectSize:
            print(selection)
            
            return
        nums_len = len(nums)
        for index in range(nums_len):
           selection.append(nums[index]) 
           self.fetchAll(nums[index + 1:], selectSize, selection, solutions)
           selection.pop(len(selection) - 1) 

            
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 2, 3]
    print(nums, " permute-->", sol.permute(nums))
