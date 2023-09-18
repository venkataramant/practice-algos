class Solution:

    def searchRange(self, nums, target):
        len_nums = len(nums)
        if len_nums == 0:
            return (-1, -1)
        left = 0
        right = len_nums
        lIndex = -1
        rIndex = -1
        while(left + 1 < right):
            print(left, right)
            mid = (left + right) // 2
            if target == nums[mid]:
                print("found at ", mid, left, right)
                if lIndex == -1:
                    lIndex = mid
                    rIndex = mid
                else:
                    lIndex = mid
                right = mid 
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
        print("checking l last one", left, right, lIndex, rIndex)
        if target == nums[left]:
            if lIndex == -1:
                lIndex = left
                rIndex = left
            elif lIndex > left:
                lIndex = left
        print("new index ", lIndex, rIndex)
        if lIndex == -1:
            return (-1, -1)
        
        print("lets find rindex")
            
        left = rIndex
        right = len(nums)
        newRIndex = -1
        while(left + 1 < right):
            print(left, right)
            mid = (left + right) // 2
            if target == nums[mid]:
                print("found at ", mid, left, right)
                newRIndex = mid
                left = mid 
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
        print("checking R last one", left, right, newRIndex)
        if newRIndex == -1:
            print("Something wrong", nums[left])
            if  right < len_nums and target == nums[right]:
                newRIndex = right
            elif target == nums[left]:
                newRIndex = left
        print(nums[lIndex:newRIndex + 1])
        return (lIndex, newRIndex)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 7, 8, 8, 8, 8, 8, 8]
    nums = [1,1,8,8,8,8,8,9,9,10 ]
    target = 8
    rng = sol.searchRange(nums, target)
    print(nums, target, rng)
