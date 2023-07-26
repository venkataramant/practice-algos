class ListNode:

     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self, head):
        newHead=None
        while(head!=None):
            newNode=ListNode(head.val)
            newNode.next=newHead
            newHead=newNode
            head=head.next
        return newHead



def printList(listX):
    index = 0
    while(listX != None):
        print(listX.val)
        listX = listX.next
        index += 1
    print("total nodes", index)


if __name__ == "__main__":
    sol = Solution()
    nums = [0,1, 2, 3, 2, 1]
    head = ListNode(nums[0])
    currentNode = head
    for val in nums[1:]:
        currentNode.next = ListNode(val)
        currentNode = currentNode.next
    head2 = head
    printList(head2)
    print(" isPalindrome -->", printList(sol.reverse(head)))

