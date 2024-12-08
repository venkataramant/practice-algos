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
        
        originalHead = head
        while(fPointer != None and fPointer.next != None):
            sPointer = sPointer.next
            fPointer = fPointer.next.next
            middleIndex += 1
        totalSize = middleIndex * 2
        if fPointer != None:
            totalSize += 1
            sPointer = sPointer.next
            print("last Node exists", totalSize)
            
        print("Middle Node middleIndex", middleIndex, "totalSize", totalSize, "midValue", sPointer.val)
        
        isPalinDrome, _ = self.verifyPalindrome(originalHead, sPointer.val, sPointer.next)
        return isPalinDrome

    def verifyPalindrome(self, originalHead, val1, middlePointer, index=1):
        if middlePointer!=None:
            print("verifyPalindrome...", val1, index, middlePointer.val)
        else:
            print("verifyPalindrome...", val1, index, "None")
        if middlePointer == None:
            if originalHead.val == val1:
                print("passed ",val1,index)
                return True, originalHead.next
            else:
                print("not matched ", originalHead.val , val1)
                return False, None
        else:
            lastCheck, newOrgHead = self.verifyPalindrome(originalHead, middlePointer.val, middlePointer.next, index + 1)
            if lastCheck:
                if newOrgHead.val == val1:
                    return True, newOrgHead.next
                else:
                    
                    print("not matched ", newOrgHead.val , val1, index, middlePointer.val, lastCheck, newOrgHead.val,"index ",index)
                    return False, None
            else:
                return lastCheck, None
        return False, None
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
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
