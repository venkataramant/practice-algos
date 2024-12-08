def findCount(nums, target):
    left = 0
    right = len(nums)
    targetIndex = -1
    while(left + 1 < right):
        mid = (left + right) // 2
        if target == nums[mid]:
            targetIndex = mid
            break
        elif target < nums[mid]:
            right = mid
        else:
            left = mid
    if targetIndex == -1:
        if nums[left] == target:
            targetIndex = left
        if right < len(nums) and nums[right] == target:
            targetIndex = right
    
    if targetIndex == -1:
        return 0
    else:
        count = 1
        left = targetIndex - 1
        right = targetIndex + 1
        while(left > 0 and nums[left] == target):
            count += 1
            left -= 1
        while(right < len(nums) and nums[right] == target):
            count += 1
            right += 1
        return count
        

def main():
  print("The number of occurrences of 5 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 5)))
  print("The number of occurrences of 20 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 20)))
  print("The number of occurrences of 1 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 1)))
  print("The number of occurrences of 19 is ---> " + str(findCount([1, 5, 5, 5, 11, 11, 15, 19, 19], 19)))


if __name__ == "__main__":
    main()
