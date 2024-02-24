class RecentCounter:

    def __init__(self):
        self.queue=[]
        self.count=0

    def ping(self, t: int) -> int:
        # print(self.queue)
        while(len(self.queue)!=0):
            # print(t,self.queue[0],t-self.queue[0])
            if t-self.queue[0]>3000:
                self.queue.pop(0)
                self.count-=1
            else:
                break
        self.queue.append(t)
        self.count+=1
        
        return self.count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)