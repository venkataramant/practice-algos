# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            print("has zero nodes")
            return False
        if head.next == None:
            print("has 1 node")
            return True
        if head.next.next == None:
            print(" has 2 nodes")
            return head.val == head.next.val
        
        sPointer = head
        fPointer = head
        middleIndex = 0
        currentNode = None
        
        newHead = None
        while(fPointer != None and fPointer.next != None):
            newNode = ListNode(sPointer.val)
            newNode.next = newHead
            newHead = newNode
            # head=head.next
            sPointer = sPointer.next
            fPointer = fPointer.next.next
            middleIndex += 1
        totalSize = middleIndex * 2
        if fPointer != None:
            totalSize += 1
            sPointer=sPointer.next
            print("last Node exists", totalSize)
            
        print("Middle Node middleIndex", middleIndex, "totalSize", totalSize, "midValue", sPointer.val)

        while(newHead!=None):
            if sPointer.val!=newHead.val:
                print(sPointer.val,newHead.val)
                return False
            sPointer=sPointer.next
            newHead=newHead.next
        
        return True
