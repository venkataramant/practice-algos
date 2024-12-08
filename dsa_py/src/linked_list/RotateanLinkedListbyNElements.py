class ListNode:

     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def rotatebyN(self, orig_head,noOfRot):
        if noOfRot==0:
            return head
        temp=orig_head
        index=0
        newHead=None
        previousNode=None
        while(temp!=None):
            if index==noOfRot:
                previousNode.next=None
                newHead=temp
                
            previousNode=temp
            temp=temp.next
            index+=1
        displayList(newHead)
        displayList(orig_head)
        displayList(previousNode)
        previousNode.next=orig_head
        displayList(newHead)
        return newHead
                
       



def displayList(listX):
    valList=list()
    while(listX != None):
        valList.append(listX.val)
        # print(listX.val)
        listX = listX.next
    print(valList,len(valList))
    return valList


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6]
    head = ListNode(nums[0])
    currentNode = head
    for val in nums[1:]:
        currentNode.next = ListNode(val)
        currentNode = currentNode.next
    head2 = head
    displayList(head2)
    print(" rotatebyN -->", displayList(sol.rotatebyN(head,3)))

