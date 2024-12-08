from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return "val:{} left:({}) right:({}))".format(self.val,self.left,self.right)
    
    @classmethod
    def construct(cls,node,level,nums):
        #print(node,level,nums)
        if not node:
            return
        len_nums=len(nums)
        lIndex=(2*level)+1
        rIndex=2*level+2
        if (lIndex<len_nums and nums[lIndex]!=None):
            print(node.val,"left", nums[lIndex],"level",level)
            node.left=TreeNode(nums[lIndex])
        if (rIndex<len_nums and nums[rIndex]!=None):
            print(node.val,"right" ,nums[rIndex],"level",level)
            node.right=TreeNode(nums[rIndex])
        if node.left:
            cls.construct(node.left,lIndex,nums)
        if node.right:
            cls.construct(node.right,rIndex,nums)
    @classmethod
    def _print_pre_order(cls, node):
        if not node:
            return
        print(node.val)
        cls._print_pre_order(node.left)
        cls._print_pre_order(node.right)
    @classmethod
    def _print_in_order(cls, node):
        if not node:
            return
        cls._print_in_order(node.left)
        print(node.val)
        cls._print_in_order(node.right)
    @classmethod
    def _print_post_order(cls, node):
        if not node:
            return
        cls._print_post_order(node.left)
        cls._print_post_order(node.right)
        print(node.val)
    @classmethod
    def _print_dfs(cls,node):
        pass
    @classmethod
    def _print_bfs_recursive(cls,queue):
        print("_print_bfs",queue)
        new_queue=[]
        if queue and len(queue)==0:
            return
        while(len(queue)>0):
            node=queue.pop(0)
            print(node.val)
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        if len(new_queue)>0:
            cls._print_bfs(new_queue)
    @classmethod
    def _print_bfs(cls,queue):
        print("_print_bfs",queue)
        
        while(len(queue)>0):
            node=queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        

if __name__=="__main__":
    nums = [1,2,3,None,5,None,4]
    root=TreeNode(nums[0])
    print(root)
    TreeNode.construct(root,0,nums)
    print(root)
    TreeNode._print_pre_order(root)
    print(root)
    TreeNode._print_bfs([root])

