from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  ans=0
  prev=R[-1]
  
  for num in R[-2::-1]:
    print(num,prev-1)
    if num>prev-1:
      ans+=1
    prev=min(num,prev-1)
    if prev<1:
      return -1
      
  return ans
