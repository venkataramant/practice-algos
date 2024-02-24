class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        c_max=0
        for x in candies:
            c_max=max(c_max,x)
        ans=[]
        for x in candies:
            ans.append(x+extraCandies>=c_max)
        # print(ans)
        return ans 