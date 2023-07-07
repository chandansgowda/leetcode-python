# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        temp = ListNode()
        temp.next = head
        fast = head
        slow = temp
        
        while n>0 and fast!=None:
            fast = fast.next
            n-=1
        
        while fast!=None:
            slow = slow.next;
            fast = fast.next
        
        slow.next = slow.next.next
        
        return temp.next
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        t = head
        nodes = 0

        while t:
            nodes+=1
            t = t.next
        
        dummy = ListNode()
        dummy.next = head
        t = dummy
        p = None
        for i in range(nodes-n+1):
            p = t
            t = t.next
        p.next=t.next
        return dummy.next
