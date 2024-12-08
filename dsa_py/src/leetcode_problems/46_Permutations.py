class Solution:

    def permute(self, nums):
        solutions = list()
        selection = list()
        self.fetchAll(nums, len(nums), selection, solutions)
        return  solutions

    def fetchAll(self, nums, selectSize, selection=None, solutions=list()):
        
        if len(selection) == selectSize:
            solutions.append(selection)
            print(selection)
            return
        nums_len = len(nums)
        for index in range(nums_len):
           new_selection = selection.copy()
           new_nums = nums.copy()
           new_selection.append(new_nums.pop(index))
           self.fetchAll(new_nums, selectSize, new_selection, solutions)

            
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 2, 3]
    print(nums, " permute-->", sol.permute(nums))
