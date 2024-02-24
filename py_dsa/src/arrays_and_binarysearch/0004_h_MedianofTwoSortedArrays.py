from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        total=len(nums1)+len(nums2)
        half=total//2
        if len(B)<len(A):
            A,B=B,A
        l,r=0,len(A)-1
        while(True):
            i= (l+r)//2 #For A ,as lenghth of A is small half-i is always valid
            j=half-i-2

            Aleft =A[i] if i>=0 else float("-infinity")
            Aright =A[i+1] if (i+1)<len(A) else float("infinity")
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright =B[j+1] if (j+1)<len(B) else float("infinity")
            if Aleft <=Bright and Bleft<=Aright:
                if total %2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2 
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1

if __name__ == '__main__':

   
    nums1 = [1,2]
    nums2 = [3,4]
    ans=2.5
    obj = Solution()
    result = obj.findMedianSortedArrays(nums1,nums2)
    
    print(result,ans,ans==result)