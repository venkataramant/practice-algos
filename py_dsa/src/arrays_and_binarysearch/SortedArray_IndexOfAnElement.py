def searchInsert(nums,target):
    left=0
    right=len(nums)
    while(left+1<right):
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid
        else:
            right=mid
    if nums[left]>=target:
        return left
    else:
        return right



def main():
  print("Index of 9 is ---> " + str(searchInsert([1, 5, 8, 9, 11, 13, 15, 19, 21], 9)))
  print("Index of 12 is ---> " + str(searchInsert([1, 5, 8, 9, 11, 13, 15, 19, 21], 12)))
  print("Index of -4 is ---> " + str(searchInsert([1, 5, 8, 9, 11, 13, 15, 19, 21], -4)))
  print("Index of 27 is ---> " + str(searchInsert([1, 5, 8, 9, 11, 13, 15, 19, 21], 27)))

if __name__=="__main__":
    main()