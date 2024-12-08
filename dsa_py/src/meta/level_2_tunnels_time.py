from typing import List
# Write any import statements here

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  tunnels=list(zip(A,B))
  tunnels.sort()
  tt_time= sum([t[1]-t[0] for t in tunnels])
  print(tt_time)
  ans =0
  rounds=K//tt_time
  remaining=K%tt_time
  ans=C*rounds
  print(tunnels)
  print(remaining,ans,tt_time)
  for t in tunnels:
    print(t,t[1]-t[0],remaining)
    if remaining <=t[1]-t[0]:
      print(f"found ther terminal{t} {t[1]-remaining}")
      ans+=t[0]+remaining
      break
    else:
      remaining-=t[1]-t[0]
  
  return ans

if __name__=="__main__":
    C = 10
    N = 2
    A = [0,1, 6]
    B = [9,13, 7]
    K = 7
    a_ans=22
    # C = 50
    # N = 3
    # A = [39, 19, 28]
    # B = [49, 27, 35]
    # K = 15
    # a_ans=35
    ans=getSecondsElapsed(C,N,A,B,K)
    print(f"ans:{ans},exepcted:{a_ans},result:{ans==a_ans}")