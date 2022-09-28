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
