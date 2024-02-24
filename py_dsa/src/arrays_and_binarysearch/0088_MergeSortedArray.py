from typing import List
class Solution:
    def best_merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        # Merge nums2 into nums1
        # m+n indicates actual size of nums1
        # start comparing next big element of nums2 to next big elment of nums1
        # if nums2 is bigger it has to occupies 0 else move big element of nums1 to next zero element 
        # [ accommodate smaller amount      of       nums1] to occupy big elment of nums1

        nums1_idx,nums2_idx, new_idx=m-1,n-1,m+n-1
        while(nums1_idx>=0 and nums2_idx>=0):
            if nums2[nums2_idx]>nums1[nums1_idx]:
                nums1[new_idx]=nums2[nums2_idx]
                nums2_idx-=1
            else:
                nums1[new_idx]=nums1[nums1_idx]
                nums1_idx-=1
            new_idx-=1
        print("before merge",nums1,nums2,nums2_idx)
        while(nums2_idx>=0):
            nums1[new_idx]=nums2[nums2_idx]
            nums2_idx-=1
            new_idx-=1
        return nums1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        currentIndex=0
        for num in nums2:
            while(currentIndex<m and nums1[currentIndex]<=num):
                currentIndex+=1
            print(nums1,currentIndex,m,num)
            if currentIndex<m:
                nums1.insert(currentIndex,num)
                nums1.pop()
                m=1
            else:
                currentIndex+=1
                nums1[currentIndex]=num
                m+=1
            print(nums1,currentIndex,m,num)
            
            num+=1
        return nums1

if __name__ =="__main__":
    sol=Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    ans1=[1,2,2,3,5,6]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    ans1=[1]
    ans=sol.merge(nums1,m,nums2,n)
    print("ans::",ans,ans1,ans==ans1) 