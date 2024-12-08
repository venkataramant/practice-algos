'''
select k numbers out of array of interegers(nums
'''


class Solution(object):

    def selectKIntegers(self, nums, k,solutions=list(),selection=list()):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        if len(selection)==k:
            print(selection,min(selection),max(selection))
            solutions.append(selection.copy())
            if len(solutions)==0:
                solutions.append(selection.copy())
            else:
                previousSelection=solutions.pop(0)
                if max(previousSelection)-min(previousSelection)>max(selection)-min(selection):
                    solutions.insert(0,selection.copy())
                    solutions.append(previousSelection)
                else:
                    solutions.insert(0,previousSelection)
                    solutions.append(selection.copy())
                     
            return
        for index in range(nums_len):
           selection.append(nums[index]) 
           self.selectKIntegers(nums[index+1:], k,solutions,selection)
           selection.pop(len(selection)-1) 
            
            
if __name__ == "__main__":
    sol = Solution()
    nums = [9,4,1,7]
    k = 2
    solutions=list()
    sol.selectKIntegers(nums, k,solutions)
    print(solutions)
