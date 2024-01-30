# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head!=None and head.next!=None:
            previous=head
            new_head=head.next
            previous.next=None
            while(new_head):
                if new_head.next:
                    temp_head=new_head.next
                    new_head.next=previous
                    previous=new_head
                    new_head=temp_head
                    
                else:
                    new_head.next=previous
                    break
            
            return new_head
        else:
            return head
    def  best_reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        return prev
        
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head!=None:
            previous,new_head=self.recursive(head)
            previous.next=None
            return new_head
        else:
            return head
    
    def recursive(self,head):
        if head.next!=None:
            previous,new_head=self.recursive(head.next)
            previous.next=head
            return head,new_head
        else:
            return head,head
        
        
        