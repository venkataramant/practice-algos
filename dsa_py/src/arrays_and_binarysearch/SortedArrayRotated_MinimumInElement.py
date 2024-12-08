def findMin(nums):
    return findMinOfRotatedBS(nums)

def findMin_simplied(nums):
        left=0
        right=len(nums)-1
        while(left+1<right):
            print(left,right)
            mid=(left+right)//2
            if nums[left]<nums[mid]:
                if nums[mid]<nums[right]:
                    return nums[left]
                else:
                    left=mid
            else:
                right=mid
        print(left,right)
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
            
def findMinOfRotatedBS(nums, left=None, right=None):
    print("findMinOfRotatedBS", nums, left, right)
    len_nums=len(nums)
    if len_nums==1:
        return nums[0]
    if len_nums==2:
        if nums[0]<nums[1]:
            return nums[0]
        else:
            return nums[1]
    if nums[0]<nums[len_nums-1]:
            return nums[0]
    if left == None:
        left = 0
        right = len(nums)
        
    while(left + 1 < right):
        print("inside ",left,right)
        lastElement = right - 1
        # print("w" , left, right, lastElement, nums[left:right])
        if nums[left] < nums[lastElement]:
            # print("non-rotated", nums[left] , nums[lastElement])
            return nums[left]
        mid = (left + right) // 2
        if nums[mid] > nums[lastElement]:
           # print("ignore left", nums[left:right], left, right, mid, nums[left:mid])
           left = mid+1
        else:
            # print("ignore right", nums[left:right], left, right, mid, nums[mid:right])
            right = mid+1
    print("after", left, right)
    if right < len(nums) and left < len(nums):
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
    elif right < len(nums):
        return nums[left]
    elif left < len(nums):
        return nums[left]
    else:
        print("something wrong", left, right)
        return None


def findMinOfRotatedBS_Recur(nums, left=None, right=None):
    print("findMinOfRotatedBS", nums, left, right)
    if left == None:
        left = 0
        right = len(nums)

    if(left + 1 > right):
        if nums[left] < nums[right]:
            return nums[left]
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            return findMinOfRotatedBS(nums, mid, right)
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
  # print("The minimum element is ---> " + str(findMin([4,5,6,7,0,1,2] )))
  # print("The minimum element is ---> " + str(findMin([11,13,15,17])))
  # print("The minimum element is ---> " + str(findMin([-5, 1, 2, 3, 4, 5, -8, -7, -6])))
  # print("The minimum element is ---> " + str(findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
  print("The minimum element is ---> " + str(findMin([4,5,1,2,3])))
  print("The minimum element is ---> " + str(findMin([11,13,15,17])))

if __name__ == "__main__":
    main()
