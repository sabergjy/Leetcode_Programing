# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        #法一：顺序合并  o(k**2*n) k是链表个数，n为链表长度  python会超时
        def mergeTwoListNode(node1, node2):
            if node1 == None and node2 == None:
                return None
            prehead = ListNode()
            curhead = prehead
            while node1 and node2:
                if node1.val <= node2.val:
                    Node_ = ListNode()
                    Node_.val = node1.val
                    curhead.next = Node_
                    curhead = curhead.next
                    node1 = node1.next
                else:
                    Node_ = ListNode()
                    Node_.val = node2.val
                    curhead.next = Node_
                    curhead = curhead.next
                    node2 = node2.next

            if node1:
                while node1:
                    Node_ = ListNode()
                    Node_.val = node1.val
                    curhead.next = Node_
                    curhead = curhead.next
                    node1 = node1.next

            if node2:
                while node2:
                    Node_ = ListNode()
                    Node_.val = node2.val
                    curhead.next = Node_
                    curhead = curhead.next
                    node2 = node2.next

            return prehead.next

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]
        

        n = len(lists)
        curListNode = lists[0]
        lists = lists[1:]
        for i in range(n-1):
            curListNode = mergeTwoListNode(curListNode,lists[0])
            lists = lists[1:]
        return curListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def mergeTwoListNode(node1, node2):
            if node1 == None and node2 == None:
                return None
            prehead = ListNode()
            curhead = prehead
            while node1 and node2:
                if node1.val <= node2.val:
                    Node_ = ListNode()
                    Node_.val = node1.val
                    curhead.next = Node_
                    curhead = curhead.next
                    node1 = node1.next
                else:
                    Node_ = ListNode()
                    Node_.val = node2.val
                    curhead.next = Node_
                    curhead = curhead.next
                    node2 = node2.next

            if node1:
                while node1:
                    Node_ = ListNode()
                    Node_.val = node1.val
                    curhead.next = Node_
                    curhead = curhead.next
                    node1 = node1.next

            if node2:
                while node2:
                    Node_ = ListNode()
                    Node_.val = node2.val
                    curhead.next = Node_
                    curhead = curhead.next
                    node2 = node2.next

            return prehead.next

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        #法二：归并合并  o(k*n*logk)
        l = 0
        r = len(lists)-1
        def margeListNodeList(l,r):
            if l == r:
                return lists[l]
            mid = (l + r)//2 #取右边
            return mergeTwoListNode(margeListNodeList(l,mid),margeListNodeList(mid+1,r))
        return margeListNodeList(0,len(lists)-1)
