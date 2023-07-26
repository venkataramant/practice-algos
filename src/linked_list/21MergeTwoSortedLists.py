# Definition for singly-linked list.
class ListNode:

     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    
    def mergeTwoListsWithPython(self, list1, list2):
        newHead = None
        currentNode = None
        while(list1 != None and list2 != None):
            if list1.val < list2.val:
                newNode = ListNode(list1.val)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                list2 = list2.next
            print("Add..",newNode.val)
            if newHead == None:
                newHead = newNode
                currentNode=newNode
            else:
                currentNode.next = newNode
                currentNode = currentNode.next
            
        nextNode = None
        if list1 != None:
            nextNode = list1
        elif list2 != None:
            nextNode = list2
        
        if(nextNode != None):
            if newHead == None:
                newHead = nextNode
                currentNode=nextNode
            else:
                currentNode.next = nextNode
        return newHead
    
    def mergeTwoListsPlain(self, list1, list2):
        newHead = None
        currentNode = None
        while(list1 != None and list2 != None):
            if list1.val < list2.val:
                newNode = ListNode(list1.val)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                list2 = list2.next
            print("Add..",newNode.val)
            if newHead == None:
                newHead = newNode
                currentNode=newNode
            else:
                currentNode.next = newNode
                currentNode = currentNode.next
            
        nextNode = None
        if list1 != None:
            nextNode = list1
        elif list2 != None:
            nextNode = list2
        
        while(nextNode != None):
            newNode = ListNode(nextNode.val)
            if newHead == None:
                newHead = newNode
                currentNode=newNode
            else:
                currentNode.next = newNode
                currentNode = currentNode.next
            nextNode = nextNode.next
        return newHead



def printList(listX):
    while(listX != None):
        print(listX.val)
        listX = listX.next


if __name__ == "__main__":
    sol = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    list2.next.next = ListNode(5)
    # printList(list1)
    # printList(list2)
    print(" mergeTwoLists -->", printList(sol.mergeTwoListsWithPython(list1, list2)))

