'''
Insert o(1)
Delete o(1)
getRandom() O(1)
'''

class OptimizedList:
    def __init__(self):
        self.list=[]
        self.keyMap=dict()
    
    def add(self,val):
        list.append(val)
        if val not in keyMap:
            keyMap[val]=set()
        keyMap[val].add(len(self.list)-1)
    def remove(self,val):
        if val in keyMap and keyMap[val]:
            index=keyMap[val].pop()
            last_index=len(self.list)-1
            last_val=self.list[-1]
            list[index]=last_val
            keyMap[last_val].add(index)
            keyMap[last_val].remove(last_index)
    
            