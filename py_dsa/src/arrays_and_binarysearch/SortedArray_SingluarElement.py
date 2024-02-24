

def singleNonDuplicate(nums, left=None,right=None):
  # from text book
  print("singleNonDuplicate ",left,right)
  if left==None:
      left = 0
      right = len(nums)
  
  if left + 1 < right:
    mid = (right + left) // 2
    print(nums[left:right], "mid-->", mid, nums[mid])
    if nums[mid] == nums[mid - 1]:
        if (((mid - 1) - left )% 2 == 1):
            print("1left array size", (mid - 1) - left, nums[left:mid - 1]) 
            return singleNonDuplicate(nums, left, mid - 1)
        else:
            print("1right array size", right - (mid + 1), nums[mid + 1:right])
            return singleNonDuplicate(nums, mid + 1, right)
        print(" something is wrong")
            
    elif nums[mid] == nums[mid + 1]:
        if ((mid - left) % 2 == 1):
            print("2left array size", mid - left, nums[left:mid]) 
            return singleNonDuplicate(nums, left, mid)
            
        else:
            print("2right array size", right - (mid + 2), nums[mid + 2:right])
            return singleNonDuplicate(nums, mid + 2, right)
        print(" something is wrong")
    else:
        print("else is missing")
  print("final;",left,right)
  if right>len(nums):
      return nums[right-1]
  elif left<len(nums):
      return nums[left]


def singleNonDuplicateFromTextBook(nums):
  # the initial value for left index is 0
  left = 0
  # the initial value for right index is the number of elements in the array
  right = len(nums)
  # left + 1 >= right will finish while loop
  while left + 1 < right:
    mid = (right + left) // 2
    
    if nums[mid] != nums[mid - 1] and (1 + mid == len(nums) or nums[mid] != nums[mid + 1]):
      # the element on the mid index is the answer
      return nums[mid]
    elif ((mid % 2) != 0 and nums[mid] == nums[mid - 1]) or ((mid % 2) == 0 and nums[mid] == nums[mid + 1]):
      # there is no sense to search in the left half of the array
      left = mid
    else:
      # there is no sense to search in the right half of the array
      right = mid
  # the element on the left index is the answer
  return nums[left]
def main():
  nums = [1, 1, 3, 3, 4, 4, 5, 8, 8]  
  nums = [0,0,1, 1,  3, 3, 4, 4, 8, 8,9] 
  print(nums)
  print("Singular Number is ---> " , singleNonDuplicate(nums))


if __name__ == "__main__":
    main()
