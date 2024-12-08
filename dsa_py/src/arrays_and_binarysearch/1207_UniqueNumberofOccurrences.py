class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        a=dict()
        for ar1 in arr:
            a[ar1]=a.get(ar1,0)+1
        unique=set()
        for _,v in a.items():
            if v in unique:
                return False
            unique.add(v) 
        return True
        