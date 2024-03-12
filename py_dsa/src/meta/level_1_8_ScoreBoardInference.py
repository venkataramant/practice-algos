from typing import List
# Write any import statements here
import math
def getMinProblemCount(N: int, S: List[int]) -> int:
  ans=0
  S.sort()
  if S[-1]%2==0:
    ans=S[-1]//2
  else:
    ans=S[-1]//2
    return ans+1
  for s in S[:-1]:
    #print(s,ans)
    if s%2==1:
      return ans+1
  return ans
