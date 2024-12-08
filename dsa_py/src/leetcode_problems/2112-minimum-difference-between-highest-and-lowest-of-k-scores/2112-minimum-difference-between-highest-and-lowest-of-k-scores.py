class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1:
            return 0
        if len(nums) == k :
            return max(nums) - min(nums)
            
        nums=sorted(nums)
        lIndex=0
        rIndex=len(nums)-k
        minDiff=None
        while(lIndex<=rIndex):
            lSection=nums[lIndex:lIndex+k]
            rSection=nums[rIndex:rIndex+k]
            lDiff=max(lSection) - min(lSection) 
            rDiff=max(rSection) - min(rSection)
            minDiff=self.compare3Values(minDiff,lDiff,rDiff)
            lIndex+=1
            rIndex-=1
        return minDiff
    def compare3Values(self,minDiff,lDiff,rDiff):
        newMin=lDiff
        if rDiff<lDiff:
            newMin=rDiff
        if minDiff==None or minDiff>newMin:
            minDiff=newMin
        return minDiff
