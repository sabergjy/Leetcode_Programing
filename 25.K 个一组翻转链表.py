# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        #1.每k个一组组，一循环（执行反转函数）
        #反转好后头尾接入链表

        def reverseKListNode(head,tail):
            pre = tail.next
            cur = head
            while pre != tail: #pre == tail时，链表已经翻转并接好了
               nex = cur.next
               cur.next = pre
               pre = cur
               cur = nex
            return tail, head
        
        if k == 1:
            return head
        
        dummyhead = ListNode()
        dummyhead.next = head
        hair = dummyhead
        pre = hair

        while head:
            ifHaveNode = pre
            for i in range(k):
                ifHaveNode = ifHaveNode.next
                if ifHaveNode == None:
                    return hair.next
            #满足有k个节点
            tail = ifHaveNode  #获取尾结点
            #翻转
            nex = ifHaveNode.next
            head, tail= reverseKListNode(head,tail)
            #拼接链表
            pre.next = head
            #tail.next = nex 这句可以不需要，因为在reverseKListNode函数中已经执行了尾节点的连接
            #新的pre和head
            pre = tail
            head = nex
        return hair.next