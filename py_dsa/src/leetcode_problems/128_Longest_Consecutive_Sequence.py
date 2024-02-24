class Solution:
    def longestConsecutive(self, nums):
        self.heapify(nums)
        sortedArray = list()
        lastArray = list()
        while(len(nums) > 0):
            newNumber = nums.pop(0)
            if len(sortedArray) != 0:
                lastNumber = sortedArray[len(sortedArray) - 1]
                if newNumber - lastNumber not in (0,1):
                    if len(sortedArray)>len(lastArray):
                        lastArray = sortedArray.copy()
                    sortedArray = list()
            if newNumber not in sortedArray:
                sortedArray.append(newNumber)
                
            self.heapifyDown(nums)
        if len(sortedArray)>len(lastArray):
            lastArray = sortedArray.copy()
        print("longestConsecutive", lastArray)
        return len(lastArray)
    
    def longestConsecutive(self, nums):
        self.heapify(nums)
        sortedArray = list()
        lastArray = list()
        while(len(nums) > 0):
            newNumber = nums.pop(0)
            if len(sortedArray) != 0:
                lastNumber = sortedArray[len(sortedArray) - 1]
                if newNumber - lastNumber not in (0,1):
                    if len(sortedArray)>len(lastArray):
                        lastArray = sortedArray.copy()
                    sortedArray = list()
            if newNumber not in sortedArray:
                sortedArray.append(newNumber)
                
            self.heapifyDown(nums)
        if len(sortedArray)>len(lastArray):
            lastArray = sortedArray.copy()
        print("longestConsecutive", lastArray)
        return len(lastArray)

    def heapifyDown(self, nums):
        if len(nums) < 1:
            return
        nums.insert(0, nums.pop())
        self.heapify(nums, 0)

    def heapify(self, nums, index=0):
       
        nums_len = len(nums)
        lIndex = index * 2 + 1
        rIndex = index * 2 + 2
        if(lIndex < nums_len):
            self.heapify(nums, lIndex)
        if(rIndex < nums_len):
            self.heapify(nums, rIndex)
        smallestChildIndex = None
        if(lIndex < nums_len and rIndex < nums_len):
            if nums[lIndex] < nums[rIndex]:
                smallestChildIndex = lIndex
            else:
                smallestChildIndex = rIndex
        elif lIndex < nums_len:
              smallestChildIndex = lIndex
        elif rIndex < rIndex:
            smallestChildIndex = rIndex
        if smallestChildIndex != None and nums[smallestChildIndex] < nums[index]:
            temp = nums[index]
            nums[index] = nums[smallestChildIndex]
            nums[smallestChildIndex] = temp
        

if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    nums = [0,3,7,2,5,8,4,6,0,1]
    # nums = [100, 200, 4] 
    print(nums, " longestConsecutive -->", sol.longestConsecutive(nums))
