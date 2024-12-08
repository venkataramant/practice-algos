class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occur=dict()
        current_max_num=None
        current_max_occ=0
        for num in nums:
            val=occur.get(num,0)+1
            occur[num]=val
            if val>=current_max_occ:
                current_max_occ=val
                current_max_num=num
                if val>len(nums)//2:
                    break
        return current_max_num

'''
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''