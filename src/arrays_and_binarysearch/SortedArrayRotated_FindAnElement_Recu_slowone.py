def search(nums, target):
    print("search", nums, target)
    return findElementInRotatedBS(nums, target)


def findElementInRotatedBS(nums, target, left=None, right=None):
    
    if left == None:
        left = 0
        right = len(nums)
    if left + 1 < right:
        lastElement = right - 1
        # if nums[left] < nums[lastElement]:
        #     print("non-rotated")
        #     return binarySearch(nums, target, left, right)
        mid = (left + right) // 2
        # print("findElementInRotatedBS", nums[left:right], left, right, mid, nums[mid])
        if target == nums[mid]:
            return mid
        if nums[left] <= target < nums[mid]:
            # print("going for left binarySearch")
            return findElementInRotatedBS(nums, target, left, mid-1)
        elif nums[lastElement] >= target > nums[mid]:
            # print("going for right binarySearch",)
            return  findElementInRotatedBS(nums, target, mid+1, right)
        else:
            leftIndex= findElementInRotatedBS(nums, target, left, mid - 1)
            if leftIndex==-1:
                return findElementInRotatedBS(nums, target, mid , right) 
            else:
                return leftIndex
        # print("not handled", left, right)

    # TODO simplify edge cases not required these many conditions
    # print("last", left, right, len(nums))
    if right < len(nums):
        # print("nums[right]", nums[right])
        if nums[right] == target:
            return right
    elif left < len(nums):
        # print("left[right]", nums[left], target)
        if nums[left] == target:
            return left
    return -1



def main():
  print("Index of 5 is ---> " + str(search([-5, 1, 2, 3, 4, 5, -8, -7, -6], 5)))
  print("Index of 6 is ---> " + str(search([-5, 1, 2, 3, 4, 5, -8, -7, -6], 6)))
  print("Index of -5 is ---> " + str(search([-5, 1, 2, 3, 4, 5, -8, -7, -6], -5)))
  print("Index of -6 is ---> " + str(search([-5, 1, 2, 3, 4, 5, -8, -7, -6], -6)))


if __name__ == "__main__":
    main()
