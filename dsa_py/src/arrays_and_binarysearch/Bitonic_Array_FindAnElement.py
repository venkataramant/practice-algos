def searchInBitonicArray(nums, target, left=None, right=None):
    print("searchInBitonicArray", target, left, right)
    if left == None:
        left = 0
        right = len(nums)
    print(nums[left:right], target)
    while(left + 1 < right):
        mid = (left + right) // 2
        if mid >= len(nums) - 1:  # for non guaranteed peak arrays
            return None
        if nums[mid] == target:
            return mid
        elif nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
            # this peak
            print("find the peak")
            lIndex = searchIncreaseBS(nums, left, mid - 1, target)
            rIndex = searchDecreaseBS(nums, mid + 1, right, target)
            print("lIndex,rIndex ", lIndex, rIndex)
            if lIndex != -1:
                return lIndex
            else:
                return rIndex
        elif nums[mid + 1] < nums[mid]:
            # searchBS on rightSide and searchInBitonicArray left side
            print("searchInBitonicArray on onLeftSide", nums[left: mid - 1])
            lIndex = searchInBitonicArray(nums, target, left, mid - 1)
            print("lIndex--> ", lIndex)
            if lIndex == -1:
                print("searchBS on RightSide", nums[mid + 1:right])
                rIndex = searchDecreaseBS(nums, mid + 1, right, target)
                print("lIndex,rIndex ", lIndex, rIndex)
                return rIndex
            else:
                return lIndex
        else:
             # searchBS on leftSide and searchInBitonicArray right side
            lIndex = searchIncreaseBS(nums, left, mid - 1, target)
            rIndex = searchInBitonicArray(nums, target, mid + 1, right)
            print("lIndex,rIndex ", lIndex, rIndex)
            if lIndex != -1:
                return lIndex
            else:
                return rIndex
    print(left, right)
    if nums[left] == target:
        return left
    elif right < len(nums) and nums[right] == target:
        return right
    else:
        return -1
    


def searchIncreaseBS(nums, left, right, target):
    print("searchIncreaseBS.1", nums[left:right], target)
    while(left + 1 < right):
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid
    print("searchIncreaseBS.2", left, right, target)
    if nums[left] == target:
        return left
    elif right < len(nums) and nums[right] == target:
        return right
    else:
        return -1


def searchDecreaseBS(nums, left, right, target):
    print("searchDecreaseBS.1", nums[left:right], target)
    while(left + 1 < right):
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            left = mid
        else:
            right = mid
    print("searchDecreaseBS.2", left, right, target)
    if nums[left] == target:
        return left
    elif right < len(nums) and nums[right] == target:
        return right
    else:
        return -1


def main2():
  print("searchInBitonicArray  is ---> " , searchInBitonicArray([3, 9, 10, 20, 17, 5, 1], 20)) 
  
  print("searchInBitonicArray  is ---> " , searchInBitonicArray([1, 3, 5, 7, 9], 6))
  
  print("searchInBitonicArray  is ---> " , searchInBitonicArray([0, 2, 1, 0], 1))
  print("searchInBitonicArray  is ---> " , searchInBitonicArray([5, 6, 7, 8, 9, 10, 3, 2, 1], 30))
  return
  print("The peak index is ---> " + str(searchInBitonicArray([-8, 1, 2, 3, 4, 5, -2, -3, -9], 2)))
  print("The peak index is ---> " + str(searchInBitonicArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 8)))
  print("The peak index is ---> " + str(searchInBitonicArray([0, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10)))


def main():
  # print("Index of 5 is ---> " + str(searchInBitonicArray([-8, 1, 2, 3, 4, 5, -2, -3, -9], 5)))
  # print("Index of 1 is ---> " + str(searchInBitonicArray([-8, 1, 2, 3, 4, 5, -2, -3, -9], 1)))
  # print("Index of -9 is ---> " + str(searchInBitonicArray([-8, 1, 2, 3, 4, 5, -2, -3, -9], -9)))
  print("Index of -1 is ---> " + str(searchInBitonicArray([-8, 1, 2, 3, 4, 5, -2, -3, -9], -1)))


if __name__ == "__main__":
    main()
