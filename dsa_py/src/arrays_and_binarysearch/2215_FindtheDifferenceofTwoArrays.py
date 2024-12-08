class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # make it unique
        def find_distint_uniq(list1,list2):
            ans=[]
            for num in list1:
                if num not in ans and num not in list2:
                    ans.append(num)
            return ans
        return [find_distint_uniq(nums1,nums2),find_distint_uniq(nums2,nums1)]
    def best_findDifference_uisng(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # make it unique use SET
        # make diff use set1-set2

        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1 - s2), list(s2 - s1)]