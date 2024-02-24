class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans=0
        p_bed=0 
        for idx in range(len(flowerbed)-1):
            c_bed=flowerbed[idx]
            n_bed=flowerbed[idx+1]
            print(idx,p_bed,c_bed,n_bed,ans)
            if p_bed==0 and c_bed==0 and n_bed==0:
                ans+=1
                p_bed=1
            else:
                p_bed=c_bed
                
        if p_bed==0 and flowerbed[-1]==0 :
            ans+=1
        return ans>=n

    def canPlaceFlowers_working(self, flowerbed: List[int], n: int) -> bool:
        ans=0
        p_bed=0 
        for idx in range(len(flowerbed)):
            # print(idx,p_bed,c_bed,ans)
            c_bed=flowerbed[idx]
            if c_bed==0:
                next_bed=0
                if idx<len(flowerbed)-1:
                    next_bed=flowerbed[idx+1]
                # print("compare", idx,p_bed,c_bed,next_bed, p_bed==0 and next_bed==0)
                if p_bed==0 and next_bed==0:
                    ans+=1
                    p_bed=1
                else:
                    p_bed=0

            else:
                p_bed=1
                #ans+=1
                
        print(ans)
        return ans>=n

'''
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''