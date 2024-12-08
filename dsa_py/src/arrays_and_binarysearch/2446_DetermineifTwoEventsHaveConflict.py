from typing import List
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        e_t1=self._convert_tuple(event1)
        e_t2=self._convert_tuple(event2)
        print(e_t1,e_t2)
        if e_t1[0]<e_t2[0]:
            return self._findout_conflict(e_t1,e_t2)
        else:
            return self._findout_conflict(e_t2,e_t1)

    def _findout_conflict(self,e_t1,e_t2):
        if e_t2[0] in range(e_t1[0],e_t1[1]+1):
            return True
        else:
            return False
    def _convert_tuple(self,event1):
        st_nums=event1[0].split(":")
        et_nums=event1[1].split(":")
        return (int(st_nums[0])*60+int(st_nums[1]),int(et_nums[0])*60+int(et_nums[1]))

    def best_haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if event2[0]>event1[1]:
            return False
        elif event2[0]>=event1[0]: #this includes the senario where event2[0]==event1[1]
            return True
        else:
            if event2[1]>=event1[0]:
                return True
            else:
                return False

if __name__ =="__main__":
    sol=Solution()
    event1 = ["01:15","02:00"]
    event2 = ["02:00","03:00"]
    # ans True
    event1 = ["01:00","02:00"]
    event2 = ["01:20","03:00"]
    # ans True
    event1 = ["10:00","11:00"]
    event2 = ["14:00","15:00"]
    # ans False
    ans=sol.haveConflict(event1,event2)
    print(event1,event2 ,"-->haveConflict::",ans)