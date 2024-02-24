from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
 
        candies=[1]*len(ratings)
        # compare with left neighbor
        for x in range(1,len(ratings)):
           if ratings[x]>ratings[x-1]:
               candies[x]=candies[x-1]+1
        print("left",ratings,candies)
        # compare with right neighbor
        for index in range(len(ratings)-2,-1,-1):
            print(index,ratings[index],ratings[index+1])
            if ratings[index]>ratings[index+1]:
               candies[index]=max(candies[index+1]+1,candies[index])
               print("u",index,candies[index])
        print("right",candies)
        return sum(candies)
            
   

if __name__ == '__main__':


   
    ratings = [1,0,2]
    ans=5
    # ratings=[1,2,87,87,87,2,1]
    # ans=13
    # ratings=[1,2,2]
    # ans=4
    obj = Solution()
    result = obj.candy(ratings)
    
    print(result,ans,ans==result)
    

