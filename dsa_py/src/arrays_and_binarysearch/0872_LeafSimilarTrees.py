# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans1=[]
        ans2=[]
        def leaves1(node):
            if node.left is None and node.right is None:
                ans1.append(node.val)
            if node.left:
                leaves1(node.left)
            if node.right:
                leaves1(node.right)
        def leaves2(node):
            if node.left is None and node.right is None:
                ans2.append(node.val)
            if node.left:
                leaves2(node.left)
            if node.right:
                leaves2(node.right)
        
        leaves1(root1)
        
        leaves2(root2)
        print(ans1,ans2)
        return ans1==ans2
        