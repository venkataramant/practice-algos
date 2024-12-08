from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        while(root):
            ans.append(root.val)
            root=root.right
        return ans

if __name__=="__main__":
    nums = [1,2,3,None,5,None,4]
    root=TreeNode(nums[0])
    level=1
    len_nums=len(nums)
    node=root
    def constr
    while(True):
        lIndex=(2*level)-1
        rIndex=2*level
        if (lIndex<len_nums):
            node.left=TreeNode(nums[lIndex])
        else:
            break
        if (rIndex<len_nums):
            node.right=TreeNode(nums[rIndex])
        else:
            break
        level+=1


    sol=Solution()
    
