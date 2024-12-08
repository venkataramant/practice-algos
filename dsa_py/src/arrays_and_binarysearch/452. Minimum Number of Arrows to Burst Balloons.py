class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        ans=1
        prev=points[0][1]
        for c_point in points[1:]:
            if c_point[0]>prev: # out of boundary
                ans+=1
                prev=c_point[1]
            else:
                prev=min(c_point[1],prev)
        return ans

        