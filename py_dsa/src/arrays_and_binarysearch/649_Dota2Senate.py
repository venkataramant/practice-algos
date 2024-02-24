class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue=[]
        d_queue=[]
        
        for index,c in enumerate(senate):
            if c=="R":
                r_queue.append(index)
            else:
                d_queue.append(index)
        len1=len(senate)
        while(r_queue and d_queue):
            #print(r_queue,d_queue)
            if r_queue[0]<d_queue[0]:
                    d_queue.pop(0)
                    r_queue.append(r_queue.pop(0)+len1)
            else:
                    r_queue.pop(0)
                    d_queue.append(d_queue.pop(0)+len1)
        #print(r_queue,d_queue)
        ans=None
        if r_queue:
            return "Radiant"
        else:
           return "Dire"

if __name__=="__main__":
    senate ="RD"
    ans="R"
    senate ="RDD"
    ans="D" 
    senate = "RRR"
    ans="R"