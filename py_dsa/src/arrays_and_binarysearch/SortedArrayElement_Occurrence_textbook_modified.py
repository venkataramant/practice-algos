def findCount(nums, target):
    leftIndex = searchBinary(nums, target, True)
    if leftIndex < 0:
        return -1
    rightIndex = searchBinary(nums, target, False)
    return rightIndex - leftIndex + 1


def searchBinary(nums, target, leftMost):
    left = 0
    right = len(nums)
    targetIndex = -1
    while(left + 1 < right):
        mid = (left + right) // 2
     
        if target == nums[mid]:
            if leftMost:
                right = mid
            else:
                left = mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid
    if targetIndex == -1:
        if nums[left] == target:
            targetIndex = left
        if right < len(nums) and nums[right] == target:
            targetIndex = right
    return targetIndex
    

def main():
  print("The number of occurrences of 5 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 5)))
  print("The number of occurrences of 20 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 20)))
  print("The number of occurrences of 1 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 1)))
  print("The number of occurrences of 19 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 19)))


if __name__ == "__main__":
    main()
