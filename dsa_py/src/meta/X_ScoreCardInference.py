from typing import List
# Write any import statements here
import math
    
def getMinProblemCount_BF(N: int, S: List[int]) -> int:
  
  answers=[]
  possible_scores=set()
  max_scroe=0
  S.sort()
  while(S and S[0]==0):
    print(S and S[0==0])
    S=S[1:]
  print(S)
  if S:
    if S[0]==1:
      answers.append(1)
      possible_scores.add(1)
      max_score=1
    elif S[0]==2:
      answers.append(2)
      possible_scores.add(2)
      max_score=2
    elif S[0]==3:
      answers.append(1)
      answers.append(2)
      possible_scores.add(1)
      possible_scores.add(2)
      possible_scores.add(3)
      max_score=3
    for score in S[1:]:
        print("inside score",answers)
        while(score>max_score):
          answers.append(2)
          possible_scores.add(max_score+1)
          possible_scores.add(max_score+2)
          max_score+=2
          
  else:
      answers.append(1)
    
  print(answers)
  return len(answers)
def getMinProblemCount_2(N: int, S: List[int]) -> int:
  
  ans=1
  possible_scores=set()
  max_scroe=0
  S.sort()
  while(S and S[0]==0):
    S=S[1:]
  if S:
    if S[0]==1:
      max_score=1
    elif S[0]==2:
      max_score=2
    elif S[0]==3:
      ans+=1
      max_score=3
    index=1
    while(index<len(S)):
        s_diff=S[index]-max_score
        if s_diff>0:
          new2s=math.ceil(s_diff/2)
          ans+=new2s
          max_score+=(2*new2s)
        index+=1
        while(index<len(S) and S[index-1]==S[index]):
          index+=1

    return ans
def getMinProblemCount(N: int, S: List[int]) -> int:
  ans=0
  S.sort()
  print(S)
  if S[-1]%2==0:
    ans=S[-1]//2
  else:
    ans=S[-1]//2
    return ans+1
  for s in S[:-1]:
    print(s)
    if s%2==1:
      return ans+1
  return ans

if __name__=="__main__":
    N = 6
    S = [1, 2, 3, 4, 5, 6]
    ans=4
    # N = 15
    # K = 2
    # M = 3
    # S = [11, 6, 14]
    # ans=1
    ans2=getMinProblemCount(N,S)
    print(ans,ans2,ans==ans2)