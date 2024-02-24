from typing import List
class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if x<=arr[0]:
            return arr[0:k]
        elif x>=arr[len(arr)-1]:
            print(-1,-k)
            return arr[-k:]
        l,r=0,len(arr)
        while(l<=r):
            # mid=l+(r-l)//2
            mid =(l+r)//2
            if x==arr[mid]:
                l,r=mid,mid
                break
            elif x>arr[mid]: # target bigger move to left
                l=mid+1
            else:
                r=mid-1
        print(l,r,arr[mid],arr[l],arr[r])
        # startIndex=l
        # if l!=r:
        #     print("checking ",x-arr[l],arr[r]-x)
        #     if abs(x-arr[l])<=abs(arr[r]-x):
        #         l,r=l,r
        #     else:
        #         l,r=r,l
        # l,r=startIndex,startIndex
        if l>r:
            l,r=r,l
        print("cons",l,r,arr[l],arr[r])
        minIndx,maxIndx=None,None
        while (l>=0 and r<len(arr)):
            print((r-l),k,arr[l],arr[r])
            if abs(arr[l]-x)<=abs(arr[r]-x):
                minIndx=l
                if not maxIndx:
                    maxIndx=l
                print("include_l",arr[l])
                if (maxIndx-minIndx)+1==k:
                    break
                l=l-1 # include l
            else:
                print("include_r",arr[r])
                maxIndx=r
                if not minIndx:
                    minIndx=r
                if (maxIndx-minIndx)+1==k:
                    break
                r=r+1 # include r
            
            
        print(minIndx,maxIndx)
        return arr[minIndx:maxIndx+1]


if __name__ == '__main__':


    arr = [1,2,3,4,5]
    k = 4
    x = 3
    ans=[1,2,3,4]
    # arr = [1,2,3,4,5]
    # k = 2
    # x = 4
    # ans=[3,4]
    arr = [1,1,1,10,10,10]
    k = 1
    x = 9
    ans=[10]
    obj = Solution()
    result = obj.findClosestElements(arr,k,x)
    
    print(result,ans,ans==result)
    

