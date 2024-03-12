# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  ans=[]
  power_of_n=0
  A1=A
  last_digit=A1 % 10
  A1=A1//10
  while(A1):
    power_of_n+=1
    last_digit=A1%10
    A1=A1//10
  print("power_of_n",A,power_of_n)
  while(True):
   
    for digit in range(1,10):
       current_ans=0
       for p in range(power_of_n,-1,-1):
          current_ans+=digit*(10**p)
          # print(current_ans,digit,p)
       print("checking",current_ans)
       if A<=current_ans<=B:
              ans.append(current_ans)
              
    if current_ans>B:
             break
    power_of_n+=1
  print(ans)
  return len(ans)
