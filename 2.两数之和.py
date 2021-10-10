# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ResNode = ListNode()
        head = ResNode
        tag = 0
        res = []
        while l1 and l2:
            ResNode.next = ListNode()
            ResNode = ResNode.next
            if tag == 1:
                if l1.val + l2.val +1 >= 10:
                   res.append(l1.val + l2.val - 9)
                   ResNode.val = l1.val + l2.val - 9 
                   l1 = l1.next
                   l2 = l2.next                
                   
                else:
                   res.append(l1.val + l2.val+1)
                   ResNode.val = l1.val + l2.val + 1
                   l1 = l1.next
                   l2 = l2.next  
                   tag = 0
      
            else:
                if l1.val + l2.val >= 10:
                   res.append(l1.val + l2.val-10)
                   ResNode.val = l1.val + l2.val -10
                   l1 = l1.next
                   l2 = l2.next  
                   tag = 1
            
                else:
                   res.append(l1.val + l2.val)
                   ResNode.val = l1.val + l2.val
                   l1 = l1.next
                   l2 = l2.next  
        
        
        if l1 == None and l2:#pyhon链表为空是None
            #操作l2
            while l2:
                ResNode.next = ListNode()
                ResNode = ResNode.next
                if tag == 1:
                    if l2.val +1 >= 10:
                       res.append(l2.val-9)
                       ResNode.val = l2.val +1 -10
                       l2 = l2.next 
                       
                    else:
                       res.append(l2.val+1)
                       ResNode.val = l2.val +1 
                       l2 = l2.next 
                       tag = 0 
                else:  
                       res.append(l2.val)
                       ResNode.val = l2.val 
                       l2 = l2.next 
                       tag = 0 
        if l2 == None and l1:
            #操作l1
            while l1:
                ResNode.next = ListNode()
                ResNode = ResNode.next
                if tag == 1:
                    if l1.val +1 >= 10:
                       res.append(l1.val-9)
                       ResNode.val = l1.val +1 -10
                       l1 = l1.next 
                       
                    else:
                       res.append(l1.val+1)
                       ResNode.val = l1.val +1 
                       l1 = l1.next 
                       tag = 0 
                else:
                       res.append(l1.val)
                       ResNode.val = l1.val 
                       l1 = l1.next 
                       tag = 0 
        
        if l1 == None and l2 == None:
            if tag == 1:
                ResNode.next = ListNode()
                ResNode = ResNode.next
                ResNode.val = 1
                res.append(1)
        return head.next
