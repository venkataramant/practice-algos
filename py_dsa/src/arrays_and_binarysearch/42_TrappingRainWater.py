from typing import List
from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        # 9 6 8 8 5 6 3
        c_p_idx=0
        n_idx=c_p_idx+1
        len_h=len(height)
        p_val=height[c_p_idx]
        peeks=deque()
        ans=[]
        while(n_idx<len_h):
            print("n_indx",n_idx)
            if p_val>=height[n_idx]:
                # Downhill ignore it
                p_val=height[n_idx]
                n_idx+=1
                
            else:
                if height[n_idx]>=height[c_p_idx]: # reached peak value bigger than current peak
                    # calculate water size and ignore queue as findout valid peek
                    print("Found actual right peak",height[n_idx],n_idx,height[c_p_idx],c_p_idx,)
                    ans.append(self.cal_size(height,c_p_idx,n_idx))
                    c_p_idx=n_idx
                    p_val=height[c_p_idx]
                    n_idx+=1
                    peeks=deque()
                    pass
                else:
                    # check with previous peek, if previous peek is smaller, replace it
                    print("peeks",peeks, "compare with last peak",n_idx,height[n_idx])
                    while(len(peeks)!=0 and height[peeks[len(peeks)-1]] <=height[n_idx]):
                            peeks.pop()
                    peeks.append(n_idx)
                    n_idx+=1


        print("final",p_val,c_p_idx,peeks)
        if len(peeks)>0:
            last_peek=peeks.pop()
            while(len(peeks)>0):
                current_peek=peeks.pop()
                ans.append(self.cal_size(height,current_peek,last_peek))
                last_peek=current_peek
            ans.append(self.cal_size(height,c_p_idx,last_peek))

        return sum(ans)
    def cal_size(self,height,lIndex,rIndex):
        min_q=min(height[lIndex],height[rIndex])
        
        temp_ans=0
        for t_height in height[lIndex:rIndex]:
            if t_height<min_q:
                temp_ans=temp_ans+min_q-t_height
        print("min_q",lIndex,rIndex,min_q,height[lIndex:rIndex],temp_ans)
        return temp_ans


if __name__ =="__main__":
    sol=Solution()
    height = [4,2,0,3,2,5]
    ans1=9
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    ans1=6
    height=[5,4,1,2]
    ans1=1
    height=[9,6,8,8,5,6,3]
    ans1=3
    ans=sol.trap(height)
    print("ans1::",ans1,ans,ans==ans1)