class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue=[]
        for indx in range(len(nums)):
            if nums[indx]==0:
                queue.append(indx)
            else:
                if len(queue)==0:
                    continue
                else:
                    nums[queue.pop(0)]=nums[indx]
                    queue.append(indx)
            #print(queue)
        
        while(len(queue)!=0):
           nums[queue.pop()]=0
                