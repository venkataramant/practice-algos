'''
1984. Minimum Difference Between Highest and Lowest of K Scores
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

 

Example 1:

Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
Example 2:

Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
 

Constraints:

1 <= k <= nums.length <= 1000
0 <= nums[i] <= 105
'''


class Solution:

    def minimumDifference(self, nums , k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1 or k == 1:
            return 0
        if len(nums) == 2 or len(nums) == k:
            return max(nums) - min(nums)
            
        nums = sorted(nums)
        lIndex = 0
        rIndex = len(nums)
        minDiff = None
        while(lIndex < rIndex):
            print(lIndex, rIndex)
            lSection = nums[lIndex:lIndex + k]
            rSection = nums[rIndex:rIndex + k]
            print(lSection, rSection)
            lDiff = max(lSection) - min(lSection) 
            rDiff = max(rSection) - min(rSection)
            minDiff = self.compare3Values(minDiff, lDiff, rDiff)
            print("minDiff..", minDiff, lDiff, rDiff)
            lIndex += 1
            rIndex -= 1
        print(lIndex, rIndex)
        return minDiff

    def compare3Values(self, minDiff, lDiff, rDiff):
        newMin = lDiff
        if rDiff < lDiff:
            newMin = rDiff
        if minDiff == None or minDiff > newMin:
            minDiff = newMin
        return minDiff

    def minimumDifference2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        previousSol = list()
        self.findAnswer(nums, k, previousSol)
        # if previousSol != None:
        #     return  max(previousSol) - min(previousSol)
        if len(previousSol) != 0:
            previousSelection = previousSol.pop()
            return max(previousSelection) - min(previousSelection)
        return 0

    def findAnswer3(self, nums, k, previousSol=None, selection=list()):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        if len(selection) == k:
            print("checking with ", previousSol, "-->", selection, min(selection), max(selection))
            
            if previousSol == None:
                previousSol = selection.copy()
            else:
                if max(previousSol) - min(previousSol) > max(selection) - min(selection):
                    previousSol = selection.copy()
                else:
                    print("ignore ", selection)
            print("new previousSol", previousSol)

        for index in range(nums_len):
           selection.append(nums[index]) 
           self.findAnswer(nums[index + 1:], k, previousSol, selection)
           selection.pop(len(selection) - 1)
    
    def findAnswer(self, nums, k, previousSol=list(), selection=list()):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        print(nums, previousSol, selection)
        if len(selection) == k:
            print("checking with ", previousSol, "-->", selection, min(selection), max(selection))
            
            if len(previousSol) == 0:
                previousSol.append(selection.copy())
            else:
                previousSelection = previousSol.pop()
                if max(previousSelection) - min(previousSelection) > max(selection) - min(selection):
                    previousSol.append(selection.copy())
                else:
                    previousSol.append(previousSelection)
            print("new previousSol", previousSol)
        previousSelection2 = None
        ans = None
        for index in range(nums_len):
           selection.append(nums[index]) 
           if self.compareWithExistingSolution(previousSol, selection):
               self.findAnswer(nums[index + 1:], k, previousSol, selection)
           selection.pop(len(selection) - 1)

    def compareWithExistingSolution(self, previousSol, selection):
        if len(previousSol) == 0:
            return True
        else:
            previousSelection = previousSol[0]
            if max(previousSelection) - min(previousSelection) > max(selection) - min(selection):
                return True
            else:
                return False
            
       
if __name__ == "__main__":
    sol = Solution()
    nums = [9, 4, 1, 7]
    nums = [90]
    nums = [64407, 3036]
    nums =[8216,18083,81861,92320,30808,4467,36436,7960]
    # nums = [41900,69441,94407,37498,20299,10856,36221,2231,54526,79072,84309,76765,92282,13401,44698,17586,98455,47895,98889,65298,32271,23801,83153,12186,7453,79460,67209,54576,87785,47738,40750,31265,77990,93502,50364,75098,11712,80013,24193,35209,56300,85735,3590,24858,6780,50086,87549,7413,90444,12284,44970,39274,81201,43353,75808,14508,17389,10313,90055,43102,18659,20802,70315,48843,12273,78876,36638,17051,20478]
    k = 8
    print("sol-->", sol.minimumDifference(nums, k))
