# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swapPair(head):
            if head == None or head.next == None:
                return head
            #递归 o(n)
            temp = head.next
            headNext = head.next.next
            temp.next = head
            head.next = swapPair(headNext)
            return temp
        
    
        
        return swapPair(head)  


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
         
        #迭代 0(n),空间o(1)
        dummyhead = ListNode()
        dummyhead.next = head
        pre = dummyhead
        while head and head.next:
            temp = head.next  #做标记1
            nodeNext = head.next.next   #做标记2  

            temp.next = head    #切换指针
            pre.next = temp    #切换指针
            head.next = nodeNext   #切换指针
            
            pre = head     #移动坐标
            head = nodeNext   #移动坐标
            
        return dummyhead.next



##!!!!!!这样切换也行
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
         
        #迭代 0(n),空间o(1)
        dummyhead = ListNode()
        dummyhead.next = head
        pre = dummyhead
        while head and head.next:
            temp = head.next  #做标记1
            nodeNext = head.next.next   #做标记2  
            
            head.next = nodeNext   #切换指针
            temp.next = head    #切换指针
            pre.next = temp    #切换指针
            
            
            pre = head     #移动坐标
            head = nodeNext   #移动坐标
            
        return dummyhead.next

