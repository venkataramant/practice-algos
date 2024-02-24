

def lastElementEqualToIndex(nums):
    left = 0
    right = len(nums)

    while(left + 1 < right):
        mid = (left + right) // 2
    
        if nums[mid] == mid and left < nums[left]:
            return mid
        elif nums[mid]> mid:
            right = mid
        else:
            left = mid
    if nums[left] == left:
        return left
    if right < len(nums) and nums[right] == right:
        return right
    return None

def firstElementEqualToIndex(nums):
    left = 0
    right = len(nums)

    while(left + 1 < right):
        mid = (left + right) // 2
    
        if nums[mid] == mid and left < nums[left]:
            return mid
        elif nums[mid]< mid:
            left = mid
        else:
            right = mid
    if nums[left] == left:
        return left
    if right < len(nums) and nums[right] == right:
        return right
    return None


def main():
  # print("firstElementEqualToIndex  is ---> " , firstElementEqualToIndex([0, 2, 5, 8, 17]))
  # print("firstElementEqualToIndex is ---> " , firstElementEqualToIndex([-10,-5,3,4,7,9]  ))
 
  print("firstElementEqualToIndex is ---> " + str(firstElementEqualToIndex([1, 5, 8, 9, 11, 13, 15, 19, 21])))
  print("firstElementEqualToIndex is ---> " + str(firstElementEqualToIndex([-8, -2, -1, 0, 2, 5, 8, 9])))
  print("firstElementEqualToIndex is ---> " + str(firstElementEqualToIndex([-1, 0, 1, 2, 3, 4, 5, 6, 7, 9])))
  print("firstElementEqualToIndex is ---> " + str(firstElementEqualToIndex([-5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
  print("firstElementEqualToIndex is ---> " + str(firstElementEqualToIndex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))


if __name__ == "__main__":
    main()
