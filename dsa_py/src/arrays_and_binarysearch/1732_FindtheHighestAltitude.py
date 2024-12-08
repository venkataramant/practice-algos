class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h_a=0
        c_a=0
        for x in gain:
            c_a=c_a+x
            h_a=max(c_a,h_a)
        return h_a
    