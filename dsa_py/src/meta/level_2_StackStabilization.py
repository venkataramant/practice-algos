from typing import List
# Write any import statements here

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
  # Write your code here
  ans=0
  def adj_cost(threshold,nums):
    if not nums:
      return 0
    if nums[-1]<threshold:
      return 0
    return B*(nums[-1]-threshold)+adj_cost(threshold-1,nums[:-1])
  for x in range(1,len(R)):
    if R[x]<=R[x-1]:
        if (A*R[x-1]+1) < adj_cost(R[x],R[:x]):
            R[x]=R[x-1]+1
        else:
            
  return ans

if __name__=="__main__":
    N = 5
    R = [2, 5, 3, 6, 5]
    A = 1
    B = 1
    a_ans=5
    # C = 50
    # N = 3
    # A = [39, 19, 28]
    # B = [49, 27, 35]
    # K = 15
    # a_ans=35
    ans=getMinimumSecondsRequired(N,R,A,B)
    print(f"ans:{ans},exepcted:{a_ans},result:{ans==a_ans}")