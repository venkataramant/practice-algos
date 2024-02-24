# Definition for singly-linked list.
class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        elif len(lists)==1:
            return lists[0]
        new_lists=[]
        for x in range(0,len(lists),2):
            if x+1==len(lists):
                new_lists.append(lists[x])
            else:
                new_lists.append(self.merge2Lists(lists[x],lists[x+1]))
        return self.mergeKLists(new_lists)
    def merge2Lists(self,l1,l2):
        new_head=None
        previous=None
        current=None
        #print(l1,new_head)
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        while( l1 and l2):
            l_value=l2.val
            if l1.val<l2.val:
                l_value=l1.val
                l1=l1.next
            else:
                l2=l2.next
            current=ListNode(l_value)
            # print(current,new_head,previous)
            if  not new_head:
                new_head=current
                previous=current
            else:
                previous.next,previous=current,current
        while(l1):
            l_value=l1.val  
            current=ListNode(l_value)
            previous.next,previous=current,current
            l1=l1.next
        while(l2):
            l_value=l2.val  
            current=ListNode(l_value)
            previous.next,previous=current,current
            l2=l2.next
        return new_head
        