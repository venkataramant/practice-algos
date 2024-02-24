from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(len(nums)):
            if x+1<len(nums) and  nums[x]==nums[x+1]:
                    return True
        return False
    def simple_containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==len(set(nums)):
            return False
        return True
    def containsDuplicate2(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        hashSet = set()

        for (i, num) in enumerate(nums):
            if num in hashSet:
                return True
            hashSet.add(num)
        return False
    