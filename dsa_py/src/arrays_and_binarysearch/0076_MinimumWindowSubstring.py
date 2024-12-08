from typing import List
class Solution:
     def minWindow(self, s: str, t: str) -> str:
        ans=None
        if len(t)>len(s):
            return ""
        ans_map=dict()
        for a in t:
            ans_map[a]=ans_map.get(a,0)+1
        print(ans_map)
        def insert_k(temp_map,ans_map,k,current_no_valid):
            if k not in ans_map:
                return current_no_valid
            c_value=temp_map.get(k,0)
            temp_map[k]=temp_map.get(k,0)+1
            if c_value+1==ans_map.get(k):
                return current_no_valid+1
            return current_no_valid

        def delete_k(temp_map,ans_map,k,current_no_valid):
            if k not in ans_map:
                return current_no_valid
            c_value=temp_map.get(k,0)
            
            print(current_no_valid,c_value,ans_map,temp_map)
            temp_map[k]=temp_map.get(k,0)-1
            if c_value-ans_map.get(k)>=0:
                print(",valid",current_no_valid)
                return current_no_valid
            print(current_no_valid-1,"c_value", c_value, c_value-ans_map.get(k))
            if current_no_valid and  current_no_valid-1<0:
                return current_no_valid-1
            return current_no_valid

        len_s=len(s)
        lIndx=0
        temp_map=dict()
        current_no_valid=0
        min_st=None
        cur_st=[]
        while(True):
            print(cur_st,lIndx, current_no_valid,temp_map)
            if ( lIndx<len_s  and (min_st is None or (len(cur_st)<len( min_st )))):
                cur_st.append(s[lIndx])
                current_no_valid=insert_k(temp_map,ans_map,s[lIndx],current_no_valid)
                lIndx+=1
            else:
                
                if len(cur_st)==0 and lIndx>=len_s :
                    break
                elif len(cur_st)==0:
                    k=cur_st.pop(0)
                    current_no_valid=delete_k(temp_map,ans_map,k,current_no_valid)
                    print(current_no_valid)

            if (current_no_valid==len(ans_map)):
                if min_st and len(min_st)>len(cur_st):
                    min_st=cur_st.copy()
                else:
                    min_st=cur_st.copy()
                print("found min_st",len(min_st))
            
        print(min_st)
        if min_st:
            return "".join(min_st)
        else:
            return ""
if __name__ =="__main__":
    sol=Solution()
    s = "ADOBECODEBANC"
    t="ABC"
    ans1 = "BANC"
    # s="ab"
    # t="a"
    # ans1="a"

    s = "cabwefgewcwaefgcf"
    t = "cae"
    ans1="cwae"

    s = "aaflslflsldkalskaaa"
    t = "aaa"
    ans1="aaa"
    ans=sol.minWindow(s,t)
    print(s,t,"-->ans::",ans,ans1==ans)