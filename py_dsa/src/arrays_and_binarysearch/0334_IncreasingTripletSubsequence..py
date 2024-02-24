from typing import List
class Solution:
   
    def increasingTriplet_working(self, arr: List[int]) -> bool:
        first=float('inf')
        second=float('inf')
        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            else:
                return True
        return False
       

if __name__ == '__main__':


    nums = [1,2,3,4,5]
    ans=True
    # nums = [5,4,3,2,1]
    # ans=False
    # nums = [2,1,5,0,4,6]
    # ans=True
    obj = Solution()
    result = obj.increasingTriplet(nums)
    
    print(result,ans,ans==result)
    

