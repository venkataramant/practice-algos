# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_ans=0
        def dfs(node):
            if not node:
                return (-1,-1)
            left=dfs(node.left)
            right=dfs(node.right)
            left_len=1+left[1]
            right_len=1+right[0]
            self.max_ans=max(self.max_ans,left_len,right_len)
            return (left_len,right_len)
        dfs(root)
        return self.max_ans

    def longestZigZag_1(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs_rec(node,pre_fix):
           
            self.ans=max(self.ans,len(pre_fix))
            #print(node,pre_fix,self.ans)
            if node:
                if pre_fix[-1]=="L":
                    dfs_rec(node.right,pre_fix+"R")
                    dfs_rec(node.left,"L")
                if pre_fix[-1]=="R":
                    dfs_rec(node.right,"R")
                    dfs_rec(node.left,pre_fix+"L")
        if root:
            dfs_rec(root.left,"L")
            dfs_rec(root.right,"R")
        return self.ans-1