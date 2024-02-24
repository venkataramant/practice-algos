class Solution:

    def findPeakElement(self, nums):
        len_nums = len(nums)
        if len_nums == 0:
            return -1
        elif len_nums == 1:
            return 0
        else:
            if nums[0] > nums[1]:
                return 0
            if nums[len_nums - 1] > nums[len_nums - 2]:
                return len_nums - 1
        left, right = 1, len_nums - 2
        while(left <= right):
            mid = (left + right) // 2
            print(left, right, nums[mid], mid)
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
                
        print("last-->", left, right)
        return -1

    def findPeakElementRec(self, nums, left=None, right=None):
        len_nums = len(nums)
        if left == None:
            if len_nums <= 1:
                return len_nums - 1
            if nums[0] > nums[1]:
                return 0
            if nums[len_nums - 2] < nums[len_nums - 1]:
                return len_nums - 1
            left = 0
            right = len_nums - 1
        print("findPeakElementRec ", left, right, right - left)
        if(left < right and right - left >= 2):
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid]:
                if nums[mid] > nums[mid + 1]:
                    print("found peak")
                    return mid
                else:
                    print("m-1<m<m+1")
                    # look from m to right (Increasing slope)
                    # look from left m-2
                    
                    rPeak = self.findPeakElementRec(nums, mid, right)
                    if rPeak == -1:
                        return self.findPeakElementRec(nums, left, mid - 1)
                    
                    return rPeak
                    
            elif nums[mid - 1] > nums[mid]:
                if nums[mid] > nums[mid + 1]:
                    print("m-1>m>m+1")
                    # look from left to m (Decreasing Slope
                    # look from m+2 to right
                    lPeak = self.findPeakElementRec(nums, left, mid)
                    if lPeak == -1:
                        return self.findPeakElementRec(nums, mid + 1, right)
                    return lPeak
                else:
                    print("m-1>m<m+1")
                    # look from left to m
                    # look from m to right
                    lPeak = self.findPeakElementRec(nums, left, mid)
                    if lPeak == -1:
                        return self.findPeakElementRec(nums, mid, right)
                    return lPeak
        
        return -1


if __name__ == "__main__":
    sol = Solution()
    
    numsList = ([5],)
    numsList = ([],)
    numsList = ([5, 6],)
    numsList = ([4, 5],)
    numsList = ([4, 4],)
    numsList = ([5, 4, 3, 4, 5],)
    numsList = ([1, 2, 3, 1],)
    # numsList = ([1,2,3,4,3],)
    # numsList = ([1, 2, 1, 3, 5, 6, 4],)
    for nums in numsList:
        peakIndex = peakIndex = sol.findPeakElement(nums)
        if peakIndex == -1:
            print("No peak for ", nums)
        else:
            print("Peak of ", nums, "is ", nums[peakIndex], "at ", peakIndex)
    
