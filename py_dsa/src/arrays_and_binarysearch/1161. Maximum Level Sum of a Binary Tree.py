# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # considering atleast one node
        sums=[]
        max_sum=float("-inf")
        level=float("inf")
        queue=[root]
        cu_level=1
        while(queue):
            len_queue=len(queue)
            total=0
            for x in range(len_queue):
                node=queue.pop(0)
                total+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sums.append(total)
            if max_sum<total:
                level=cu_level
                max_sum=total
            cu_level+=1
        print(level,max_sum,sums)
        return level
