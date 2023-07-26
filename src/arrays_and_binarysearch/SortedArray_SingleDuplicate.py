
def findSingleDuplicate2(nums):
  # from text book
  left = 0
  right = len(nums)

  while left + 1 < right:
    mid = (right + left) // 2

    if nums[mid] == nums[mid - 1]:
      return nums[mid]
    elif nums[mid] > mid:
      left = mid
    else:
      right = mid

  return nums[left]
  
def findSingleDuplicate(nums, newDuplicateNum=None):
    print(newDuplicateNum, " is in ", nums)
    nums_len = len(nums)
    if newDuplicateNum != None:
        if nums_len == 0:
            return None
        elif nums_len == 1:
            if nums[0] == newDuplicateNum:
                return newDuplicateNum
            return None
        elif nums_len > 1:
            if nums[0] == newDuplicateNum:
                return newDuplicateNum
            if nums[nums_len - 1] == newDuplicateNum:
                return newDuplicateNum
    left = 0
    right = nums_len
    newDuplicateNumIndex = (left + right) // 2
    ld = findSingleDuplicate(nums[0:newDuplicateNumIndex], nums[newDuplicateNumIndex])
    rd = findSingleDuplicate(nums[newDuplicateNumIndex + 1:], nums[newDuplicateNumIndex])
    if ld != None:
        return ld
    else:
        return rd


def main():
  print("Duplicate Number is ---> " , findSingleDuplicate([1, 2, 3, 4, 4, 5, 6, 7]))
  print("Duplicate Number is ---> " , findSingleDuplicate([1, 1, 2, 3, 4, 5]))
  print("Duplicate Number is ---> " , findSingleDuplicate([1, 2, 3, 4, 5, 5]))
  print("Duplicate Number is ---> " , findSingleDuplicate([1, 1]))
  print("Duplicate Number is ---> " , findSingleDuplicate([1]))


if __name__ == "__main__":
    main()
