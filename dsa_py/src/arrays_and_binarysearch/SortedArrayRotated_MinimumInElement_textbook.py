def searchInBitonicArray(nums, target):
  bitonicPoint = findBitonicPoint(nums)
  indexInLeftPart = ascendingBinarySearch(nums, 0, bitonicPoint, target)
  
  if -1 != indexInLeftPart:
    return indexInLeftPart
  
  indexInRightPart = descendingBinarySearch(nums, bitonicPoint + 1, len(nums), target)
  
  if -1 != indexInRightPart:
    return indexInRightPart

  return -1


def findPivot(nums):
  # the initial value for left index is 0
  left = 0
  # the initial value for right index is the number of elements in the array
  right = len(nums)
  # left + 1 >= right will finish while loop
  while left + 1 < right:
    mid = (right + left) // 2
    
    if nums[mid - 1] > nums[mid]:
      # mid is the index to answer
      return mid
    elif nums[left] < nums[mid]:
      # there is no sense to search in the left half of the array
      left = mid
    else:
      # there is no sense to search in the right half of the array
      right = mid
  # left is the answer
  return left


def findMin(nums):
    pivot = findPivot(nums)
        
    return min(nums[0], nums[pivot])


def main():
  print("The minimum element is ---> " + str(findMin([-5, 1, 2, 3, 4, 5, -8, -7, -6])))
  print("The minimum element is ---> " + str(findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


if __name__ == "__main__":
    main()
