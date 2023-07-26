def findMin(nums):
    print("findMin", nums)
    return findMinOfRotatedBS(nums)


def findMinOfRotatedBS(nums, left=None, right=None):
    
    if left == None:
        left = 0
        right = len(nums)

    if left + 1 < right:
        lastElement = right - 1
        if nums[left] < nums[lastElement]:
            return nums[left]
        mid = (left + right) // 2
        if nums[mid] > nums[lastElement]:
            return findMinOfRotatedBS(nums, mid + 1, right)
        else:
            return findMinOfRotatedBS(nums, left, mid)
    #TODO simplify edge cases not required these many conditions
    if right < len(nums) and left < len(nums):
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
    elif right < len(nums):
        return nums[right]
    elif left < len(nums):
        return nums[left]
    else:
        print("something wrong", left, right)
        return None


def main():
  print("The minimum element is ---> " + str(findMin([4, 5, 6, 7, 0, 1, 2])))
  print("The minimum element is ---> " + str(findMin([11, 13, 15, 17])))
  print("The minimum element is ---> " + str(findMin([-5, 1, 2, 3, 4, 5, -8, -7, -6])))
  print("The minimum element is ---> " + str(findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


if __name__ == "__main__":
    main()
