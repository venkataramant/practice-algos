# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root and root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root


    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find_ancestors(node, target):
            
            if node.val==target.val:
                #print(node.val,target.val)
                return [node]
            if node.left:
                l_ancestors=find_ancestors(node.left,target)
                
                if l_ancestors is not None:
                    #print(node.val,target.val,"l",len(l_ancestors)," adding ",node.val)
                    l_ancestors.append(node)
                    return l_ancestors
    
            if node.right:
                r_ancestors=find_ancestors(node.right,target)
                
                if r_ancestors is not None:
                    print(node.val,target.val,"r",len(r_ancestors)," adding ",node.val)
                    r_ancestors.append(node)
                    return r_ancestors
            return None
        p_ansestors =find_ancestors(root, p)
        q_ansestors =find_ancestors(root, q)

        #print(len(p_ansestors),"----",len(q_ansestors))
        ans=None
        while(p_ansestors and q_ansestors):
            p_ans=p_ansestors.pop()
            q_ans=q_ansestors.pop()
            #print("inside",p_ans.val,q_ans.val)
            if p_ans.val==q_ans.val:
                ans=q_ans
                print("ans",ans.val)
            else:
                return ans
            
        return ans

        