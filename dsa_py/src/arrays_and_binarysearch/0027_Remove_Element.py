class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 0 1 2 2  3 0 4 2

        # 0 1 3 0 4 _ _ _ 

        # Q 5,6 7
        que=[]
        actual=0
        for indx in range(len(nums)):
            if nums[indx]==val:
                # nums[indx]="_"
                que.append(indx)
            else:
                actual+=1
                if len(que)==0:
                    # nothing queue to replace
                    continue
                else:
                    # move the position
                    nums[que.pop(0)]=nums[indx]
                    nums[indx]="-"
                    que.append(indx)
            print(nums)
        return actual

#Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
        
                 


             

        