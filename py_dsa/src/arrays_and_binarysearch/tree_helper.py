class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def construct(node,level,nums):
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
            construct(node.left,lIndex,nums)
        if node.right:
            construct(node.right,rIndex,nums)

def _print_pre_order( node):
        if not node:
            return
        print(node.val)
        _print_pre_order(node.left)
        _print_pre_order(node.right)
def _print_in_order( node):
        if not node:
            return
        _print_in_order(node.left)
        print(node.val)
        _print_in_order(node.right)
def _print_post_order( node):
        if not node:
            return
        _print_post_order(node.left)
        _print_post_order(node.right)
        print(node.val)

def _print_bfs_recursive(queue):
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
            _print_bfs(new_queue)
def _print_bfs(queue):
        print("_print_bfs",queue)
        
        while(len(queue)>0):
            node=queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)