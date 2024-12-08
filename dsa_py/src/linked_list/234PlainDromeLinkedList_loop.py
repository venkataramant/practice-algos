class ListNode:

     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # go to middle ,while going, convert first half reverse and compare both of them.
    def isPalindrome(self, head):
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
            print("last Node exists", totalSize)
            
        print("Middle Node middleIndex", middleIndex, "totalSize", totalSize, "midValue", sPointer.val)
        print("reverse", printList(newHead))
        print("reverse2", printList(newHead))
        if fPointer != None:
            sPointer=sPointer.next
        print("2nd half", printList(sPointer))
        print("2nd half2", printList(sPointer))
        while(newHead!=None):
            if sPointer.val!=newHead.val:
                print(sPointer.val,newHead.val)
                return False
            sPointer=sPointer.next
            newHead=newHead.next
        
        return True

    def verifyPalindrome(self, currentNode, nextNode):
        
        return None


def printList(listX):
    index = 0
    myList = list()
    while(listX != None):
        # print(listX.val)
        myList.append(listX.val)
        listX = listX.next
        index += 1
    print("total nodes", index)
    return myList


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 2, 3, 2, 1]
    # nums = [1, 2, 3, 4,5,4, 3, 2, 1]
    head = ListNode(nums[0])
    currentNode = head
    for val in nums[1:]:
        currentNode.next = ListNode(val)
        currentNode = currentNode.next
    head2 = head
    printList(head2)
    print(" isPalindrome -->", sol.isPalindrome(head2))

