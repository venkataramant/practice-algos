# Definition for a binary tree node.
from typing import List,Optional
import tree_helper as th

class Solution:
    def rightSideView(self, root: Optional[th.TreeNode]) -> List[int]:
        ans=[]
        queue=[root]
        while(queue):
            print(queue,queue[len(queue)-1].val)
            len_queue=len(queue)
            for x in range(len_queue):
                node=queue.pop(0)
                if x==len_queue-1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
    def rightSideView_recur(self, root: Optional[th.TreeNode]) -> List[int]:
        ans={}

        def pre_order(node,level=0):
            if not node:
                return
            ans[level]=node.val
            if node.left:
                pre_order(node.left,level+1)
            if node.right:
                pre_order(node.right,level+1)
        pre_order(root)
        key=0
        ans_list=[]
        while(True):
            if key in ans:
                ans_list.append(ans[key])
                key+=1
                continue
            else:
                break
        return ans_list


if __name__=="__main__":
    nums = [1,2,3,None,5,None,4]
    ans=[1,3,4]
    root=th.TreeNode(nums[0])
    level=1
    len_nums=len(nums)
    node=root
    th.construct(root,0,nums)
    sol=Solution()
    ans2=sol.rightSideView(root)
    print(ans2,ans==ans2)
    
