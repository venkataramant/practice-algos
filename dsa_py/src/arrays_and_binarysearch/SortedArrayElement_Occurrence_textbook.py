def findCount(nums, target):
    count = 0
    count = searchBinary(nums, target, count)
    return count


# EDGE cases logic is missing...has to FIX @TODO
def searchBinary(nums, target, count, left=None, right=None):
    if left == None:
        left = 0
        right = len(nums)
    while(left + 1 < right):
        mid = (left + right) // 2
        if target == nums[mid]:
                leftCount = searchBinary(nums, target, 1, left=left, right=mid - 1)
                rightCount = searchBinary(nums, target, 1, left=mid + 1, right=right)
                return leftCount + rightCount 
        elif target < nums[mid]:
            # right = mid
            return searchBinary(nums, target, count, left=left, right=mid)
        else:
            # left = mid
            return searchBinary(nums, target, count, left=mid, right=right)
    
    if left < len(nums) and nums[left] == target:
        return count + 1
    if right < len(nums) and nums[right] == target:
        return count + 1
    return 0
    

def main():
  print("The number of occurrences of 5 is ---> " + str(findCount([2, 5, 5, 5, 5, 6], 5)))
 
  print("The number of occurrences of 5 is ---> " + str(findCount([5, 5, 5, 5, 5, 11, 11, 15, 19, 19], 5)))
  print("The number of occurrences of 20 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 20)))
  print("The number of occurrences of 1 is ---> " + str(findCount([1, 1, 5, 5, 5, 11, 11, 15, 19, 19], 1)))
  print("The number of occurrences of 19 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19, 19, 19], 19)))


if __name__ == "__main__":
    main()
