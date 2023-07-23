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
        self.heapifyUp(nums)

    def heapifyUp(self, nums):
        childIndex = len(nums) - 1
        while(childIndex > 0):
            parentIndex = childIndex // 2
            if nums[parentIndex] > nums[childIndex]:
                temp = nums[parentIndex ]
                nums[parentIndex ] = nums[childIndex]
                nums[childIndex ] = temp
            else:
                break
            childIndex = parentIndex
        
    def deleteMinHeap(self, nums):
        minVal = nums.pop(0)
        if len(nums) == 0:
            return minVal, nums
        nums.insert(0, nums.pop())
        return  minVal, self.heapifyDown(nums)

    def heapifyDown(self, nums):
        parentIndex = 0
        nums_len = len(nums)
        while(parentIndex < nums_len):
            
            lcIndex = 2 * parentIndex + 1
            rcIndex = 2 * parentIndex + 2
            print("heapifyDown", nums, lcIndex, rcIndex)
            if lcIndex < nums_len and rcIndex < nums_len:
                if  nums[parentIndex] > nums[lcIndex] and nums[parentIndex] > nums[rcIndex]:
                    print("parent is min ")
                    break
            if lcIndex < nums_len  and nums[parentIndex] > nums[lcIndex]:
                print("left child is min")
                temp = nums[parentIndex ]
                nums[parentIndex ] = nums[lcIndex]
                nums[lcIndex ] = temp
                parentIndex = lcIndex
                continue
            elif rcIndex < nums_len  and nums[parentIndex] > nums[rcIndex]:
                    print("right child is min")
                    temp = nums[parentIndex ]
                    nums[parentIndex ] = nums[rcIndex]
                    nums[rcIndex ] = temp
                    parentIndex = rcIndex
                    continue
            else:
                print("parent has no children")
                break
                    
        return nums


if __name__ == "__main__":
    sol = Solution()
    
    nums = [5, 3, 4]
    nums = [7, 4, 3, 2]
    # nums = [8,6,6,4,2,1, 3, -1, -3, 5, 3, 6, 7]
    print(nums, " minHeap-->", sol.minHeap(nums))
