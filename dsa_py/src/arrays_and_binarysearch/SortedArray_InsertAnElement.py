def insertIntoBS(nums, newNum):
    left = 0
    right = len(nums)
    ans = None
    while(left + 1 < right):
        mid = (left + right) // 2
        if nums[mid] == newNum:
            ans = mid
            break
        elif nums[mid] < newNum:
            left = mid
        else:
            right = mid
    if ans == None:
        if nums[left] >= newNum:
            ans = left
        else:
            ans = right
    nums.insert(ans, newNum)
    print(nums)
    return ans


def main():
  print("Index of 9 is ---> " + str(insertIntoBS([1, 5, 8, 9, 11, 13, 15, 19, 21], 9)))
  print("Index of 12 is ---> " + str(insertIntoBS([1, 5, 8, 9, 11, 13, 15, 19, 21], 12)))
  print("Index of -4 is ---> " + str(insertIntoBS([1, 5, 8, 9, 11, 13, 15, 19, 21], -4)))
  print("Index of 27 is ---> " + str(insertIntoBS([1, 5, 8, 9, 11, 13, 15, 19, 21], 27)))


if __name__ == "__main__":
    main()
