from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  
  def distance(x,y):
    dist =0
    if x!=y:
      if x>y:
        dist=x-y
      else:
        dist=y-x
      if dist >N//2:
        dist=N-dist
    return dist
  ans=0
  prev=1
  for code in C:
      print(ans,code)
      ans+=distance(code,prev)
      prev=code
  return ans
  
