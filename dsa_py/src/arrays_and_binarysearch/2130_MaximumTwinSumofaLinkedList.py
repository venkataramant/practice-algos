# Definition for singly-linked list.
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        if head.next.next==None:
            return head.val+head.next.val
        
        s_ptr=head
        f_ptr=head
        queue=[]
        ans=float("-inf")
        while(s_ptr):
            # print(s_ptr.val,queue)
            if (f_ptr):
                queue.append(s_ptr.val) # Adding first values
                f_ptr=f_ptr.next.next
            else:
                ans=max(ans,s_ptr.val+queue.pop())

            s_ptr=s_ptr.next
        return ans


if __name__ =="__main__":
    sol=Solution()

    nums = [5,4,2,1]
    previous=None
    head=None
    for num in  nums[::-1]:
        head=ListNode(num,previous)
        previous=head
    print(head.val)
    node=head
    while(node):
        print(node.val)
        node=node.next
   
    correct_ans=6
    
    ans=sol.pairSum(head)
    print(head ,"-->pairSum::",ans,correct_ans,ans==correct_ans)