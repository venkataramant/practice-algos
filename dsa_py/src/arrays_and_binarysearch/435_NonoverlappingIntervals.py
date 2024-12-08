from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        print(intervals)
        intervals.sort()
        print(intervals)
        ans=0
        if intervals:
            prev=intervals[0]
            for c_inter in intervals[1:]:
                if c_inter[0]<prev[1]:
                    ans+=1
                    if c_inter[1]<prev[1]:
                        prev=c_inter
                else:
                    prev=c_inter
                
        return ans


if __name__ == '__main__':
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    ans=1
    intervals = [[1,2],[1,2],[1,2]]
    ans=2
    intervals = [[1,2],[2,3]]
    ans=0
    obj = Solution()
    result = obj.eraseOverlapIntervals(intervals)
    print(intervals,"eraseOverlapIntervals",result,ans,ans==result)