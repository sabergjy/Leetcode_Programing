# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode()
        curhead = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                Node_ = ListNode()
                Node_.val = l1.val
                curhead.next = Node_
                curhead = curhead.next
                l1 = l1.next
            else:
                Node_ = ListNode()
                Node_.val = l2.val
                curhead.next = Node_
                curhead = curhead.next
                l2 = l2.next
        
        if l1:
            while l1:
                Node_ = ListNode()
                Node_.val = l1.val
                curhead.next = Node_
                curhead = curhead.next
                l1 = l1.next  
        
        if l2:
            while l2:
                Node_ = ListNode()
                Node_.val = l2.val
                curhead.next = Node_
                curhead = curhead.next
                l2 = l2.next


        return prehead.next

    

        