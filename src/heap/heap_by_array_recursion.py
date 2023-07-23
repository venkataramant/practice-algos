'''
heapyArray
'''


class Solution:

    def minHeap(self, nums):
        minHeapTree = list()
        for num in nums:
            self.insertMinHeap(minHeapTree, num)
            # print(minHeapTree, num)
        return self.sortMinHeap(minHeapTree)

    def sortMinHeap(self, minHeapTree):
        sortedList = list()
        while(len(minHeapTree) > 0):
            minVal, minHeapTree = self.deleteMinHeap(minHeapTree)
            sortedList.append(minVal)
            print("sorted..", minVal, minHeapTree)
        return sortedList

    def insertMinHeap(self, nums, nextNumber):
        nums.append(nextNumber)
        childIndex = len(nums) - 1
        self.heapifyUp(nums, childIndex)

    def heapifyUp(self, nums, index):
        
        if index < 0:
            return 
        parentIndex = index // 2
        if nums[parentIndex] > nums[index]:
            temp = nums[parentIndex ]
            nums[parentIndex ] = nums[index]
            nums[index ] = temp
        else:
            return
        return self.heapifyUp(nums, parentIndex)
        
    def deleteMinHeap(self, nums):
        minVal = nums.pop(0)
        if len(nums) == 0:
            return minVal, nums
        nums.insert(0, nums.pop())
        return  minVal, self.heapifyDown(nums)

    def heapifyDown(self, nums,parentIndex = 0):
        nums_len = len(nums)
        if parentIndex >= nums_len:
            return nums
        else:   
            lcIndex = 2 * parentIndex + 1
            rcIndex = 2 * parentIndex + 2
            print("heapifyDown", nums,nums[parentIndex], lcIndex, rcIndex)
            if lcIndex < nums_len and rcIndex < nums_len:
                if nums[parentIndex] <= nums[lcIndex]   and nums[parentIndex]<=nums[rcIndex] :
                    print("parent is min ")
                    return nums
                elif nums[parentIndex] > nums[lcIndex]:
                    print("left child is min")
                    temp = nums[parentIndex ]
                    nums[parentIndex ] = nums[lcIndex]
                    nums[lcIndex ] = temp
                    return self.heapifyDown(nums,lcIndex)
                else:
                    print("right child is min")
                    temp = nums[parentIndex ]
                    nums[parentIndex ] = nums[rcIndex]
                    nums[rcIndex ] = temp
                    return self.heapifyDown(nums,rcIndex)
            if lcIndex < nums_len  and nums[parentIndex] > nums[lcIndex]:
                print("left child is min")
                temp = nums[parentIndex ]
                nums[parentIndex ] = nums[lcIndex]
                nums[lcIndex ] = temp
                return self.heapifyDown(nums,lcIndex)
            elif rcIndex < nums_len  and nums[parentIndex] > nums[rcIndex]:
                    print("right child is min")
                    temp = nums[parentIndex ]
                    nums[parentIndex ] = nums[rcIndex]
                    nums[rcIndex ] = temp
                    return self.heapifyDown(nums,rcIndex)
            else:
                print("parent has no children")
                return nums
                    
        return nums


if __name__ == "__main__":
    sol = Solution()
    
    nums = [5, 3, 4]
    nums = [7, 4, 3, 2,-1,2,-1]
    # nums = [8,6,6,4,2,1, 3, -1, -3, 5, 3, 6, 7]
    print(nums, " minHeap-->", sol.minHeap(nums))
