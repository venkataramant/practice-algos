from typing import ListNode, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            s_ptr=head
            f_ptr=head
            previous=None
            while(True):
                if f_ptr.next is None:
                    # reached end of list ODD
                    previous.next=s_ptr.next
                    print("deleted",s_ptr.val)
                    break
                elif f_ptr.next.next is None:
                    # reached end of list # EVEN 
                    print("deleted",s_ptr.next.val)
                    s_ptr.next=s_ptr.next.next
                    break
                else:
                    # proceed to further
                    previous,s_ptr,f_ptr=s_ptr,s_ptr.next,f_ptr.next.next
            return head
        else:
            return None
    def best_deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
    
        original_head = head
        l, r = head, head
        prev = head

        while r and r.next:
            prev = l
            l = l.next
            r = r.next.next
        
        prev.next = l.next
        return original_head
        
        