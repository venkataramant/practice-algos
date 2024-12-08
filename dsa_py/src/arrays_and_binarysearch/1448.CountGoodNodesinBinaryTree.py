# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def recur(node,c_h,res):
            if node:
                if node.val>=c_h:
                    res.append(node.val)
                recur(node.left,max(node.val,c_h),res)
                recur(node.right,max(node.val,c_h),res)
        if root:
            res=[]
            recur(root,root.val,res)
            return len(res)
        else:
            return 0



        