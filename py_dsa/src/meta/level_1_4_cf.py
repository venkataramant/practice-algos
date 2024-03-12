from typing import List
import math

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  
  ans=0
  S.sort()
  prev=0
  current=S[0]
  available=current-K-1-0
  if 1<=available<=K:
      ans+=1
  elif available>K:
      ans+=math.ceil(available/(K+1))
  print(current,prev,ans,available)
  prev=current 
  for current in S[1:]:
    available=current-K-1-prev-K
    if 1<=available<=K:
      ans+=1
    elif available>K:
        ans+=math.ceil(available/(K+1))
    
    prev=current
    print(current,ans)
  available=N-(prev+K)
  if 1<=available<=K:
      ans+=1
  elif available>K:
      ans+=math.ceil(available/(K+1))
  print(N,prev,ans,available)
  return ans
if __name__=="__main__":
    # N = 10
    # K = 1
    # M = 2
    # S = [2, 6]
    # ans=3
    N = 20
    K = 3
    M = 3
    S = [10, 1,6, 14]
    ans=1
    ans2=getMaxAdditionalDinersCount(N,K,M,S)
    print(ans,ans2,ans==ans2)