def findBitonicPoint(nums):
    left = 0
    right = len(nums)
    if right < 2:
        return -1
    while(left + 1 < right):
 
        mid = (left + right) // 2
        if mid>=len(nums)-1: # for non guaranteed peak arrays
            return None
        if nums[mid] >= nums[mid - 1] and nums[mid] >= nums[mid + 1]:
            return mid
        elif nums[mid] <= nums[mid - 1]:
            right = mid
        else:
            left = mid
    return left


def main():
  print("findBitonicPoint  is ---> " , findBitonicPoint([1,3,5,7,9]))
  print("findBitonicPoint  is ---> " , findBitonicPoint([0, 2, 1, 0]))
  
  print("The peak index is ---> " + str(findBitonicPoint([-8, 1, 2, 3, 4, 5, -2, -3, -9])))
  print("The peak index is ---> " + str(findBitonicPoint([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
  print("The peak index is ---> " + str(findBitonicPoint([0, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
    

if __name__ == "__main__":
    main()
