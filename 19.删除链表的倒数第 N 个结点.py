# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        prehead = ListNode()
        prehead.next = head
        preNode = prehead
        curNode = head
        finalNode = head
        #移动n-1个
        if n == 1:
            finalNode = head
        for i in range(n-1):
            finalNode = finalNode.next

        #最后一直移动，当finalNode到尾节点，则curNode就是要删除的那个节点
        while finalNode.next:
            preNode = preNode.next
            curNode = curNode.next
            finalNode = finalNode.next
        
        pNext = curNode.next
        preNode.next = pNext
        curNode.next = None
        return prehead.next
