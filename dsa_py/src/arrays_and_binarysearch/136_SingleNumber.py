from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        uniques=set()
        for num in nums:
            if num in uniques:
                uniques.remove(num)
            else:
                uniques.add(num)
        return uniques.pop()
    
    # python way of doing
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)

'''

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 
 '''